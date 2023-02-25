from django.urls import path
from . import views

urlpatterns = [
    path('hello_api_view', views.HelloApiView.as_view()),
]