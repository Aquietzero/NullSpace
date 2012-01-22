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

    categories = categoriesForIndex(blog_list)
    tags = tagsForIndex(blog_list)

    # archieve

    return render_to_response('index.html', 
            { 'blogs'      : blogs,
              'categories' : categories,
              'tags'       : tags,
            })


def tagsForIndex(blog_list):

    tag_list = Tag.objects.all()
    tags = {}
    for tag in tag_list:
        tags[tag.name] = 0

    for blog in blog_list:
        for tagName in blog.getTags():
            tags[tagName] += 1

    return [ {'name':name, 'size':tags[name]} for name in tags ]



def categoriesForIndex(blog_list):
    category_list = Category.objects.all()
    categories = []
    for category in category_list:
        size = 0
        for blog in blog_list:
            if blog.getCategory() == category.name:
                size += 1
        categories.append({ 'name' : category.name,
                            'size' : size })

    return categories
