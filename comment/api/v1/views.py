from rest_framework import viewsets

from .serializers import CommentSerializer
from .permissions import IsOwnerOrReadOnly
from comment.models import Comment

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.order_by('created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly,]

    def filter_queryset(self, queryset):
        post_id = self.kwargs.get('post_pk')
        return queryset.filter(post__id=post_id)

