from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/v1/', include('topic.api.v1.urls')),

]