# Generated by Django 2.2.7 on 2019-12-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=256, verbose_name='Name')),
                ('user_number', models.CharField(max_length=256, verbose_name='number phone')),
                ('user_email', models.EmailField(blank=True, max_length=256, null=True, verbose_name='email')),
            ],
        ),
    ]
