from django.urls import path

from . import views

app_name = 'linksorg'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_us, name='about_us'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration_form'),
    path('my_links/', views.MyLinksListView.as_view(), name='user_links'),
    path('add_link/', views.add_link, name='add_link'),
    path('delete_link/<int:pk>/', views.delete_link, name='delete_link'),
    path('category/create/', views.add_category, name='category_create'),
    path('categories/', views.MyCategoriesListView.as_view(), name='user_categories'),
    path('category/<int:pk>/details', views.MyCategoryDetailView.as_view(), name='category_details'),
    path('category/<int:pk>/update', views.CategoryUpdate.as_view(), name='category_update'),
    path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),
]
