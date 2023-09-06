# from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse
from django.template.loader import render_to_string
from django_filters.views import FilterView
# from django.views.generic import FormView

from .models import Link
from .forms import RegisterForm, AddLinkForm
from .filters import LinkFilter


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


class MyLinksListView(LoginRequiredMixin, FilterView):
    model = Link
    template_name = 'linksorg/my_links.html'
    paginate_by = 10
    filterset_class = LinkFilter

    def get_queryset(self):
        return Link.objects.filter(user__id=self.request.user.id).order_by('-date_time')


def add_link(request):
    data = {}
    if request.method == 'POST':
        link_form = AddLinkForm(request.POST)
        if link_form.is_valid():
            data['form_is_valid'] = True
            link = link_form.cleaned_data['url_link']
            category = link_form.cleaned_data['category']
            definition = link_form.cleaned_data['short_definition']
            important = link_form.cleaned_data['important']
            new_link = Link(user_id=request.session.get('_auth_user_id'),short_definition=definition, url_link=link, category=category, important=important)
            new_link.save()
        else:
            data['form_is_valid'] = False
    else:
        link_form = AddLinkForm()
    data['html_form'] = render_to_string(template_name='linksorg/link_form.html',
                                         context={'form': link_form}, request=request)
    return JsonResponse(data)
