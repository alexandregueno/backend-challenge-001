from django.conf.urls import url, include
from rest_framework_nested import routers

from comment.api.v1.views import CommentViewSet

router = routers.SimpleRouter()
router.register(r'comment', CommentViewSet, basename='comment')

urlpatterns = [
    url(r'^', include(router.urls)),
]
