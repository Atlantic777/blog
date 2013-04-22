from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
     url(r'^$', blog_roll),
     url(r'^post/(?P<post_id>\d+)/', blog_single_post),
)
