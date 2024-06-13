from django.urls import path
from . import views

# URl patterns for the dashboard app
urlpatterns = [
    path('', views.dashboard, name='home'),
    path('dashboard/', views.dashboard, name='home'),
]
