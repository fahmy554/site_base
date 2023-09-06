from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import  Category,Store,Store_Image,Post


admin.site.register(Category)
admin.site.register(Store)
admin.site.register(Store_Image)
admin.site.register(Post)