"""
API V1: Accounts Serializers
"""
###
# Libraries
###
from post.models import Post
from rest_framework import serializers
from topic.api.v1.serializers import TopicSerializer

###
# Serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id","title","author","content", "created_at", "updated_at","topic")