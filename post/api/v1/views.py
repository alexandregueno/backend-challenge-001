from rest_framework import viewsets,serializers
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from post.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('created_at')
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def filter_queryset(self, queryset):
        topic_slug= self.kwargs.get('topic_slug')
        return queryset.filter(topic__slug=topic_slug)