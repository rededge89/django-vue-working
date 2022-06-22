# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommunityViewSet, RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'community', CommunityViewSet)

urlpatterns = [
    path("", include(router.urls))
]