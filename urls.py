from django.conf.urls.defaults import patterns, include, url
from NullSpace import settings
from NullSpace.blogs.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NullSpace.views.home', name='home'),
    # url(r'^NullSpace/', include('NullSpace.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/blogs/blog/add/$', 'NullSpace.blogs.admin_views.add_blog'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', index),
    (r'^index/$', index),
    (r'^index/archieve$', archieve),
    (r'^index/about$', about),
    (r'^index/(?P<slug>[\w-]*/\d{4}-\d{2}-\d{2}/)$', post),
    (r'^index/(?P<slug>[\w-]*/\d{4}-\d{2}-\d{2}/)next$', nextPost),
    (r'^index/(?P<slug>[\w-]*/\d{4}-\d{2}-\d{2}/)prev$', prevPost),
    (r'^index/category/(?P<category>\w+)$', postsForCategory),
    (r'^index/created/(?P<year>\d{4})/(?P<month>\w*)$', postsForCreated),
    (r'^index/tags/(?P<tagName>\w+)$', postsForTag),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root':settings.MEDIA_ROOT }),
)
