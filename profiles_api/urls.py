from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello_viewset', views.HelloViewSet, basename='hello_viewset')


urlpatterns = [
    path('hello_api_view', views.HelloApiView.as_view()),
    path('', include(router.urls))
]