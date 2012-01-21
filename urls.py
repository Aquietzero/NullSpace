from django.conf.urls.defaults import patterns, include, url
from NullSpace import settings
from NullSpace.blogs.admin_views import *
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
    (r'^index/$', index),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root':settings.MEDIA_ROOT }),
)
