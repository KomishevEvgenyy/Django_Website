# Generated by Django 2.2.7 on 2019-12-12 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_number',
            new_name='number',
        ),
    ]
