from django.conf.urls import include
from django.conf.urls import url
from pblog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
   
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^post/$', views.add_new_post, name='post'),
    url(r'^postdetail/(?P<post_id>[0-9])$', views.post_detail, name='post_detail'),
]
