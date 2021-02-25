
from django.contrib import admin
from .models import Comment

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at","post")

