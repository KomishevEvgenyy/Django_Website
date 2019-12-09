from django.db import models


class User(models.Model):
    user_name = models.CharField('Name', max_length=256)
    user_number = models.CharField('number phone', max_length=256)
    user_email = models.EmailField('email', max_length=256, null=True, blank=True)

    def __str__(self):
        return self.user_name




