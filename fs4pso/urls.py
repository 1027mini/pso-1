from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^write/$', views.write, name='write'),
#    url(r'^$', views.main_post, name='main_post'),
    url(r'^subject/(?P<subject_id>\d+)$', views.subject, name='subject'),
    url(r'^$', views.main_subject, name='main_subject'),
    url(r'^login/$', views.login, name='login'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^find/$', views.find, name='find'),
#    url(r'^look/$', views.look, name='look'),
    url(r'^look/(?P<post_id>\d+)/$', views.looks, name='looks'),
    url(r'^likes/(?P<post_id>\d+)/$', views.likes, name='likes'),
    
]