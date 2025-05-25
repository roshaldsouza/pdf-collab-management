from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # Custom login path pointing to your template location
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True), name='login'),
    
    path('signup/', views.SignUpView.as_view(), name='signup'),
     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]