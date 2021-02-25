from django.conf.urls import url, include
from rest_framework_nested import routers

from post.api.v1.views import PostViewSet

router = routers.SimpleRouter()
router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    url(r'^', include(router.urls)),
]
