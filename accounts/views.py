from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# Register new users
class register(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


# Login existing users
class login(LoginView):                                                              
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm


# Logout existing users
class logout(LogoutView):
    pass