from django.db import models


class User(models.Model):
    username = models.CharField('Name', max_length=256)
    first_name = models.CharField('first name', max_length=256)
    email = models.EmailField('email', max_length=256, null=True, blank=True)
    last_name = models.CharField('last name', max_length=256)
    password = models.CharField('password', max_length=256)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username




