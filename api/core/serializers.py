from rest_framework import serializers
from .models.community import Community
from .models.recipe import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "id",
            "name",
            "ingredients",
            "picture",
            "difficulty",
            "prep_time",
            "prep_guide",
        )


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = (
            "id",
            "name",
            "payroll_code",
            "badge_prefix",
            "new_development",
            "currently_supported",
            "address_1",
            "address_2",
            "city",
            "state",
            "zip_code",
        )
