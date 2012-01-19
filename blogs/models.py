from django.db import models

# A blog has many comments but belongs to only
# one category.
class Blog(models.Model):
    title = models.CharField(max_length = 70)
    body = models.TextField()
    slug = models.CharField(max_length = 100)
    created = models.DateField()
    tags = models.ManyToManyField(Tag)
    category = model.ForeignKey(Category)

    def __unicode__(self):
        return self.title



# A comment belongs to a unique blog.
class Comment(models.Model):
    content = models.TextField()
    email = models.EmailField()
    gravatar = models.UrlField()
    visitor = models.CharField()
    created = models.DateField()
    approved = models.BooleanField()
    blog = models.ForeignKey(Blog)

    def __unicode__(self):
        return self.visitor + '-' + self.created
    


# A tag can belong to many blogs while a blog can
# also have so many tags.
class Tag(models.Model):
    name = models.CharField(30)
    rank = models.IntegreField()

    def __unicode__(self):
        return self.name



# A category has many blogs.
class Category(models.Model):
    name = models.CharField()
    size = models.IntegreField()

    def __unicode__(self):
        return self.name
