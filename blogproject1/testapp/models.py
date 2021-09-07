from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=256,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=CustomManager()
    class Meta:
        ordering=('-created',)


    #whenever if u are call all() it calls Internally __str__() method
    #whenevr if u are going to publish post display title
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

#model related to comments section
class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=22)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return 'Commented by {} on {}'.format(self.name,self.post)

class hydjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class blorejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()
class chennaijobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()
class punejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class Movie(models.Model):
    rdate=models.DateField()
    moviename=models.CharField(max_length=30)
    hero=models.CharField(max_length=30)
    heroine=models.CharField(max_length=30)
    rating=models.IntegerField()
