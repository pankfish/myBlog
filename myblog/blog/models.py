from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
import datetime

# Create your models here.
class Author(User):
    class Meta:
        proxy = True


class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    topic = models.CharField(max_length=40, default="General")
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)
    content = RichTextField(),
    description = models.TextField(blank=True, null=True)
    blog_img = models.ImageField(null=True, blank = True, upload_to="images/")


    def get_absolute_url(self):
        return reverse("blog:post-view", kwargs={"id": self.id})


