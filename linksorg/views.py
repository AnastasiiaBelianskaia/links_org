# from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from django_filters.views import FilterView

from .filters import LinkFilter
from .forms import AddLinkForm, CategoryForm, RegisterForm
from .models import Category, Link


def index(request):
    return render(request, 'linksorg/index.html')


def about_us(request):
    return render(request, 'linksorg/about_us.html')


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
            new_link = Link(user_id=request.session.get('_auth_user_id'), short_definition=definition, url_link=link,
                            category=category, important=important)
            new_link.save()
        else:
            data['form_is_valid'] = False
    else:
        link_form = AddLinkForm()
    data['html_form'] = render_to_string(template_name='linksorg/link_form.html',
                                         context={'form': link_form}, request=request)
    return JsonResponse(data)


def update_link(request, pk):
    old_link = Link.objects.get(id=pk)
    if request.method == 'POST':
        update_form = AddLinkForm(request.POST, instance=old_link)
        if update_form.is_valid():
            updated = update_form.save(commit=False)
            updated.date_time = timezone.now()
            updated.save()
            return redirect('linksorg:user_links')
    else:
        update_form = AddLinkForm(instance=old_link)
    return render(request, 'linksorg/change_link_form.html', {'form': update_form})


def delete_link(request, pk):
    link = Link.objects.get(id=pk)
    if request.method == 'POST':
        link.delete()
    return redirect('linksorg:user_links')


def add_category(request):
    data = {}
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            data['form_is_valid'] = True
            name = category_form.cleaned_data['name']
            new_category = Category(name=name)
            new_category.save()
        else:
            data['form_is_valid'] = False
    else:
        category_form = CategoryForm()
    data['html_form'] = render_to_string(template_name='linksorg/category_form.html',
                                         context={'form': category_form}, request=request)
    return JsonResponse(data)


def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
    return redirect('linksorg:user_links')


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
        return Link.objects.select_related('category').filter(user__id=self.request.user.id).order_by('-date_time')


class MyCategoriesListView(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = 'linksorg/my_categories.html'
    paginate_by = 10

    def get_queryset(self):
        return Category.objects.all()


class MyCategoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Category
    template_name = 'linksorg/category_details.html'

    def get_object(self, queryset=None):
        category = Category.objects.get(id=self.kwargs['pk'])
        return category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = Link.objects.filter(category__id=self.kwargs['pk'])
        return context


class CategoryUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Category
    fields = ['name']
    template_name = 'linksorg/category_update_form.html'
    success_url = reverse_lazy('linksorg:user_categories')
    success_message = 'Category has been updated!'

    def get_object(self, queryset=None):
        category_initial = Category.objects.get(id=self.kwargs['pk'])
        return category_initial
