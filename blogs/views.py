from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.paginator import *
from NullSpace.blogs.models import *

def index(request):
    blog_list = Blog.objects.order_by('created')

    # pagination
    paginator = Paginator(blog_list, 5)
    page = request.GET.get('page')

    if page:
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
    else:
        blogs = paginator.page(1)

    # categories
    categories = Category.objects.all()

    # archieve

    return render_to_response('index.html', 
            { 'blogs'      : blogs,
              'categories' : categories,
              })
