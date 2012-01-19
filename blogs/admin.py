from django.contrib import admin
from NullSpace.blogs.models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created',)
    date_hierarchy = 'created'
    fields = ('title', 'body', 'created', 'tags', 'category',)
    filter_horizontal = ('tags',)  # better for many to many selection.
    #raw_id_fields = ('category',) # better for foreign keys selection.



admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
