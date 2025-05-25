from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.shortcuts import redirect
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('documents:dashboard')  # Points to your dashboard

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')  # Redirect to login after signup
    template_name = 'accounts/signup.html'

def custom_logout(request):
    logout(request)
    return redirect('login')