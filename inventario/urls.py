from django.urls import path
from . import views

urlpatterns = [
    path('contact/<str:name>', views.contact),
    path('categorias/', views.categorias),
    path('', views.index),
    ###
    path('categorias/', views.categoria_list, name='categoria_list'),
]
