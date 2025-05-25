from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('upload/', views.UploadPDFView.as_view(), name='upload'),
    path('<int:pk>/', views.PDFDetailView.as_view(), name='pdf_detail'),
    path('<int:pk>/share/', views.SharePDFView.as_view(), name='share_pdf'),
    path('shared/<str:share_link>/', views.SharedPDFView.as_view(), name='shared_pdf'),
]