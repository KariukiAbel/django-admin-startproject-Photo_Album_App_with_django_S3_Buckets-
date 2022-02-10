from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('view/<str:pk>', views.viewPhoto, name='view'),
    path('add/', views.addPhoto, name='add'),
    
]