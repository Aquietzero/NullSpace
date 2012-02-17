#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from NullSpace import settings
from NullSpace.blogs.views import *
from NullSpace.feeds import ArchiveFeed

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
    (r'^archive/$', archieve),
    (r'^about/$', about),
    (r'^post/(?P<slug>[\w-]*/\d{4}-\d{2}-\d{2}/)$', post),
    (r'^post/(?P<slug>[\w-]*/\d{4}-\d{2}-\d{2}/)next$', nextPost),
    (r'^post/(?P<slug>[\w-]*/\d{4}-\d{2}-\d{2}/)prev$', prevPost),
    (r'^category/(?P<category>\w+)$', postsForCategory),
    (r'^created/(?P<year>\d{4})/(?P<month>\w*)$', postsForCreated),
    (r'^tags/(?P<tagName>\w+)$', postsForTag),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root':settings.MEDIA_ROOT }),
)

urlpatterns += patterns('',
    (r'^feed/latest/$', ArchiveFeed()),        
)
