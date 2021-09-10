from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name='index'),
    path("rand/", views.randomdino, name='rand'),
    path("herbivorous/", views.herbivores, name='herbivorous'),
    path('carnivorous/', views.carnivores, name='carnivorous'),
    path('omnivorous/', views.omnivorous, name='omnivorous'),

]