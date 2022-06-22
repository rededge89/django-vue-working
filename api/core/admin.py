from django.contrib import admin

from .models.community import Community
from .models.recipe import Recipe


admin.site.register(Recipe)
admin.site.register(Community)