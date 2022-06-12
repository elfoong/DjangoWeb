import os
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='web/images/%Y/%m/%d/', blank=True)
    attatched_file = models.FileField(upload_to='web/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


# 모델 메소드 정의(오버라이드)
def __str__(self):
    return f'[{self.pk}]{self.title} :: {self.author}'


def get_absolute_url(self):
    return f'/recipe/{self.pk}/'


def get_file_name(self):
    return os.path.basename(self.attached_file.name)
