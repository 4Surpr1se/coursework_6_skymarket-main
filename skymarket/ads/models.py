from django.conf import settings
from django.db import models

# from skymarket.users.models import User
from users.models import User


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    image = models.ImageField(upload_to='images/ads/', null=True, blank=True)
    title = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    description = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.text

