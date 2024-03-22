from django.urls import path
from cat_app import views

app_name = 'cat_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('pets/', views.pets, name='pets')
]


