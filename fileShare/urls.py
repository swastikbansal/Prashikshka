from django.urls import path,include
from . import views

urlpatterns = [
    path('file/',views.fileShare,name='fileShare'),
]
