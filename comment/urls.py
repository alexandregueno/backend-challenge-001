from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/v1/', include('comment.api.v1.urls'))
]