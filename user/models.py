from django.db import models
from django.conf import settings


class User(models.Model):
    username = models.CharField('Name', max_length=256)
    first_name = models.CharField('first name', max_length=256)
    email = models.EmailField('email', max_length=256, null=True, blank=True)
    last_name = models.CharField('last name', max_length=256)
    password = models.CharField('password', max_length=256)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    # расширение для модели User добавление дополнительных данных
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)





