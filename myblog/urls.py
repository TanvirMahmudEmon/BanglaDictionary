from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^myblog/$', views.post_list, name='post_list'),  # http://127.0.0.1:8000/myblog/myblog/
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
