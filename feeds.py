from django.contrib.syndication.views import Feed
from NullSpace.blogs.models import Blog 
import markdown

class ArchiveFeed(Feed):

    title = "NullSpace"
    link = "/archieve/"
    description = "NullSpace's latest posts."

    def items(self):
        return Blog.objects.all()

    def item_link(self, item):
        return '/post/' + item.slug

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown.markdown(truncateWords(item.body, 300, '...'))


def truncateWords(content, length=200, sufix='...'):
    if len(content) < length:
        return content
    else:
        return ''.join(content[:length]) + sufix

