from django.db import models

# A tag can belong to many blogs while a blog can
# also have so many tags.
class Tag(models.Model):
    name = models.CharField(max_length = 30)
    rank = models.IntegerField()

    def __unicode__(self):
        return self.name



# A category has many blogs.
class Category(models.Model):
    name = models.CharField(max_length = 30)
    size = models.IntegerField()

    def __unicode__(self):
        return self.name



# A blog has many comments but belongs to only
# one category.
class Blog(models.Model):
    title = models.CharField(max_length = 70)
    body = models.TextField()
    slug = models.CharField(max_length = 100)
    created = models.DateField()
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title



# A comment belongs to a unique blog.
class Comment(models.Model):
    content = models.TextField()
    email = models.EmailField()
    gravatar = models.URLField()
    visitor = models.CharField(max_length = 50)
    created = models.DateField()
    approved = models.BooleanField()
    blog = models.ForeignKey(Blog)

    def __unicode__(self):
        return self.visitor + '-' + self.created
