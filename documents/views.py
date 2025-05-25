from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, View
from django.urls import reverse, reverse_lazy
from .models import PDFDocument, Comment
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, ListView):
    model = PDFDocument
    template_name = 'documents/dashboard.html'
    context_object_name = 'documents'

    def get_queryset(self):
        """Return only the current user's documents with recent comments"""
        return PDFDocument.objects.filter(owner=self.request.user).order_by('-created_at')

class UploadPDFView(LoginRequiredMixin, CreateView):
    model = PDFDocument
    fields = ['title', 'file']
    template_name = 'documents/upload.html'
    success_url = reverse_lazy('documents:dashboard')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Add recent documents and comments for the sidebar"""
        context = super().get_context_data(**kwargs)
        context['recent_docs'] = PDFDocument.objects.filter(
            owner=self.request.user
        ).order_by('-created_at')[:5]
        context['recent_comments'] = Comment.objects.filter(
            document__owner=self.request.user
        ).order_by('-created_at')[:5]
        return context

class PDFDetailView(LoginRequiredMixin, DetailView):
    model = PDFDocument
    template_name = 'documents/pdf_detail.html'
    context_object_name = 'document'

    def post(self, request, *args, **kwargs):
        """Handle new comments"""
        self.object = self.get_object()
        content = request.POST.get('content', '').strip()
        guest_name = request.POST.get('guest_name', 'Anonymous').strip()
        
        if content:
            Comment.objects.create(
                document=self.object,
                content=content,
                guest_name=guest_name if guest_name else 'Anonymous',
                author=request.user if request.user.is_authenticated else None
            )
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(document=self.object).order_by('-created_at')
        return context

class SharePDFView(LoginRequiredMixin, View):
    def get(self, request, pk):
        """Generate shareable link for a PDF"""
        document = get_object_or_404(PDFDocument, pk=pk, owner=request.user)
        
        if not document.shareable_link:
            document.shareable_link = uuid.uuid4().hex[:20]
            document.save()
            
        share_url = request.build_absolute_uri(
            reverse('documents:shared_pdf', args=[document.shareable_link]))
            
        return render(request, 'documents/share.html', {
            'document': document,
            'share_url': share_url
        })

class SharedPDFView(View):
    def get(self, request, share_link):
        """View for shared PDF with comments"""
        document = get_object_or_404(PDFDocument, shareable_link=share_link)
        comments = Comment.objects.filter(document=document).order_by('-created_at')
        
        return render(request, 'documents/shared_pdf.html', {
            'document': document,
            'comments': comments
        })

    def post(self, request, share_link):
        """Handle new comments on shared PDF"""
        document = get_object_or_404(PDFDocument, shareable_link=share_link)
        guest_name = request.POST.get('guest_name', 'Anonymous').strip()
        content = request.POST.get('content', '').strip()
        
        if content:  # Only save if there's actual content
            Comment.objects.create(
                document=document,
                guest_name=guest_name if guest_name else 'Anonymous',
                content=content,
                author=request.user if request.user.is_authenticated else None
            )
        
        return redirect('documents:shared_pdf', share_link=share_link)