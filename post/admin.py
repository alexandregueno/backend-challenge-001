from django.contrib import admin
from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ("topic", "title", "created_at", "updated_at")
