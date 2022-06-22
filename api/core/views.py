from rest_framework import viewsets

from .serializers import CommunitySerializer
from .models.community import Community

from .serializers import RecipeSerializer
from .models.recipe import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class CommunityViewSet(viewsets.ModelViewSet):
    serializer_class = CommunitySerializer
    queryset = Community.objects.all()
