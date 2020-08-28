from django.urls import path
from cam import views

urlpatterns = [
    path('', views.Index, name='index'),
]
