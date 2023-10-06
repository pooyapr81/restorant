from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    content = RichTextField()
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='blogs/', null=True, blank=True)
    category = models.ForeignKey("Category", related_name='blog', on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField("Tag", related_name="blogs", null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    published = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey("Blog", related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

