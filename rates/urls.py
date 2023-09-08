from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RateViewSet


router = DefaultRouter()
router.register('api', RateViewSet)


urlpatterns = [
    path('',include(router.urls))
]