from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from NullSpace.blogs.models import *
from NullSpace.blogs.forms import *
from datetime import *

def index(request):

    blog_list = Blog.objects.order_by('created').reverse()

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
    archieve = archieveForIndex(blog_list)


    return render_to_response('index.html', 
            { 'blogs'      : blogs,
              'categories' : categories,
              'tags'       : tags,
              'archieve'   : archieve,
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



def archieveForIndex(blog_list):

    thisYear = datetime.now().year
    blog_list = Blog.objects.order_by('created')
    oldestYear = blog_list[0].created.year

    archieve = {}
    for year in range(oldestYear, thisYear+1):
        archieve[year] = {}
        for month in range(1, 13):
            archieve[year][month] = []

    for blog in blog_list:
        archieve[blog.created.year][blog.created.month].append(blog)

    return [ {'year'   : year,
              'months' : [ {'month' : archieve[year][month][0].created.strftime('%B'), 
                            'size'  : len(archieve[year][month]) 
                           } for month in archieve[year] if len(archieve[year][month]) != 0 ]
             } for year in archieve ]


@csrf_exempt
def post(request, slug):

    post = Blog.objects.get(slug=slug)

    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            saveComment(comment, post)
            return HttpResponseRedirect('/index/' + slug)
        else:
            return HttpResponseRedirect('/index/' + slug)
    else:
        comment = CommentForm()
         
    blog_list = Blog.objects.order_by('created').reverse()
    categories = categoriesForIndex(blog_list)
    tags = tagsForIndex(blog_list)
    archieve = archieveForIndex(blog_list)

    return render_to_response('post_solo.html', { 
        'post'       : post, 
        'comment'    : comment,
        'tags'       : tags,
        'categories' : categories,
        'archieve'   : archieve,
    })



def saveComment(comment, post):

    c = Comment()
    c.approved = False
    c.blog = post
    c.created = datetime.now().strftime('%Y-%m-%d %H:%M')
    c.visitor = comment.cleaned_data['visitor']
    c.website = comment.cleaned_data['website']
    c.email   = comment.cleaned_data['email']
    c.content = comment.cleaned_data['content']
    c.save()
