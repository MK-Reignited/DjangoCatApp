from django.urls import path
from cat_app import views

app_name = 'cat_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/', views.cats, name='cats')
]


