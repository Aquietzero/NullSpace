from NullSpace.blogs.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.defaultfilters import slugify
#from django.contrib.admin.views.decorator import staff_member_required

def add_blog(request):
    if request.POST:
        title = request.POST['title']
        created  = request.POST['created']
        slug  = slugify(title) + '/' + slugify(created) + '/'
        request.POST['slug'] = slug

        blog = Blog(request.POST)
        blog.save()
        render_to_response('admin/change_list.html')

    else:
        render_to_response('admin/blogs/change_form.html')
