from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photos/grid/', views.photos_grid, name='photos_grid'),
    path('photos/new/', views.new_photo, name='new_photo'),
    path(r'photos/<pk>/', views.full_photo, name='full_photo'),
    path('photos/cat/<selected_category>/', views.category_view, name='category_view'),
    path('photos/cat_list/list/', views.cat_view, name='cat_list'),
]
