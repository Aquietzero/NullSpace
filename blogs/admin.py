from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render_to_response
from NullSpace.blogs.models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'category', 'slug')
    date_hierarchy = 'created'
    fields = ('title', 'body', 'created', 'tags', 'category',)
    filter_horizontal = ('tags',)  # better for many to many selection.
    #raw_id_fields = ('category',) # better for foreign keys selection.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'created', 'approved')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(Category)
