from telnetlib import LOGOUT
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView, View
from .models import User
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login


# Registration
class UserRegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        login(self.request, form.auth_user)
        return super(UserRegistrationView, self).form_valid(form)


# Login
class UserLoginView(FormView):
    form_class = LoginForm
    template_name = "user/login.html"
    success_url = reverse_lazy('product_show')

    def form_valid(self, form):
        login(self.request, form.auth_user)
        return super(UserLoginView, self).form_valid(form)


# LogOut
class LogoutView(View):
    def get(self, request):
        LOGOUT(request)
        return reverse_lazy('home_index')


# Home_index
class ShowIndexView(TemplateView):
    template_name = 'base/index.html'

    def get(self, request, *args, **kwargs):
        print(request.user)
        return super(ShowIndexView, self).get(request, *args, **kwargs)
