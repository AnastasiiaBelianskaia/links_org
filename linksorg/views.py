# from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# from django.views.generic import FormView

from .forms import RegisterForm


def index(request):
    return render(request, 'linksorg/index.html')


def about_us(request):
    return render(request, 'linksorg/about_us.html')


class UserRegistrationView(SuccessMessageMixin, generic.FormView):
    form_class = RegisterForm
    fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('linksorg:index')
    success_message = 'Welcome!'

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super().form_valid(form)
