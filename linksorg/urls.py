from django.urls import path

from . import views

app_name = 'linksorg'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_us, name='about_us'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration_form'),
    path('my_links/', views.MyLinksListView.as_view(), name='user_links'),
    path('add_link/', views.add_link, name='add_link'),
]
