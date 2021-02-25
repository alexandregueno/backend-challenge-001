"""
API V1: Accounts Serializers
"""
###
# Libraries
###
from topic.models import Topic
from rest_framework import serializers


###
# Serializers
class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ("name", "title","slug", "author", "created_at", "updated_at")