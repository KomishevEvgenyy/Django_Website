from django.db import models


class User(models.Model):
    name = models.CharField('Name', max_length=256)
    number = models.CharField('number phone', max_length=256)
    email = models.EmailField('email', max_length=256, null=True, blank=True)

    def __str__(self):
        return self.user_name




