from django.urls import path, include
from . import views as views

urlpatterns = [
    path('get_model/', views.get_model),
    path('search/', views.search)
]
