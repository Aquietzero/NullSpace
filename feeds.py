from django.contrib.syndication.views import Feed
from NullSpace.blogs.models import Blog 

class ArchiveFeed(Feed):

    title = "NullSpace"
    link = "/archieve/"
    description = "NullSpace's latest posts."

    def items(self):
        return Blog.objects.order_by('created').reverse()[:5]

    def item_link(self, item):
        return '/post/' + item.slug

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return 'hello'

