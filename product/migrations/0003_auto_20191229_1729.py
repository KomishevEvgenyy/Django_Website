# Generated by Django 3.0.1 on 2019-12-29 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20191224_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='picture',
            new_name='image',
        ),
    ]