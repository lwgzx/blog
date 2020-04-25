# Create your models here.
from django.db import models


class Category(models.Model):
    category_name = models.CharField(default="", max_length=20)
    category_info = models.CharField(default="", max_length=100)


class Tag(models.Model):
    tag_name = models.CharField(default="", max_length=20)
    tag_info = models.CharField(default="", max_length=100)


class Entry(models.Model):
    title = models.CharField(default="", max_length=128)
    author = models.CharField(default="", max_length=10)
    img = models.ImageField(upload_to='blog_img', null=True, blank=True, verbose_name='博客配图')
    body = models.TextField(default="")
    abstract = models.TextField(default="", max_length=256, null=True, blank=True)
    visiting = models.PositiveIntegerField(default=0)
    category = models.CharField(default="", max_length=20)
    tags = models.CharField(default="", max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)


class User(models.Model):
    user_name = models.CharField(default="", max_length=20)
    password = models.CharField(default="", max_length=20)
    email = models.CharField(default="", max_length=50)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    last_login_time = models.DateTimeField('上次登录时间', auto_now=True)
