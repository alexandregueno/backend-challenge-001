"""
API V1: Accounts Serializers
"""
###
# Libraries
###
from comment.models import Comment
from rest_framework import serializers

###
# Serializers
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("id","title","author","content", "created_at", "updated_at", "post")