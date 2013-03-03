from django.db import models
import os.path

# Create your models here.

class Category( models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return "<Category {title}>".format(title=self.title)

    def get_absolute_url(self):
        return "/category/{category}".format(category=self.slug)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Categories"

class Visualization( models.Model):
    title = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    html = models.TextField()

    def __unicode__(self):
        return "<Visualization {title}>".format( title=self.title)

    def get_absolute_url(self):
        return "/visualization/{visual}".format(visual=self.slug)

    class Meta:
        ordering = ["title"]

class Picture( models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(upload_to="/home/stupschwartz/ArtCode/media/images/", max_length=200)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return "<Picture {title}>".format(title=self.title)

    def get_absolute_url(self):
        return "/static/images/{fileName}".format(fileName=os.path.basename(self.file.name))

    class Meta:
        ordering = ["title"]

class PostManager( models.Manager):
    def shuffle(self,**kwargs):
        import random
        posts = list( super( PostManager, self).get_query_set().filter( **kwargs))
        random.shuffle(posts)
        return posts

class Post( models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    images = models.ManyToManyField( Picture)
    category = models.ManyToManyField( Category)
    visualization = models.ManyToManyField( Visualization, blank=True)

    objects = PostManager()

    def __unicode__(self):
        return "<Post {title}>".format(title=self.title)

    def get_absolute_url(self):
        return "/posts/{slug}".format(slug=self.slug)

    class Meta:
        ordering = ["posted"]


