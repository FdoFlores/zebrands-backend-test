from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class IndexView(TemplateView):
    template_name = "frontend/index.html"

class LoginViewCustom(LoginView):
    template_name = 'frontend/login.html'
    redirect_authenticated_user = True
