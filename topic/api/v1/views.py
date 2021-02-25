from rest_framework import viewsets

from .serializers import TopicSerializer
from .permissions import IsOwnerOrReadOnly
from topic.models import Topic
from rest_framework import permissions

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.order_by('created_at')
    serializer_class = TopicSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'slug'