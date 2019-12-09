from django.contrib import admin

from .models import Categories, Brand, ObjectForCategories

admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(ObjectForCategories)

# Register your models here.
