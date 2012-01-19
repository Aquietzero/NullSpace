from django.contrib import admin
from NullSpace.blogs.models import *

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
