from django.urls import path,include
from . import views

urlpatterns = [
    path('upload',views.fileUpload,name='fileUpload'),
    path('',views.fileView,name='fileView'),
]
