from django.contrib import admin
from django.urls import path, include #add include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Crud.urls')), #add this line
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('post/', views.postview, name='post'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]