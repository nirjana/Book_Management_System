from django.contrib import admin
from bms.models import *


from .models import Image
# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['id', 'photo', 'date']

 

admin.site.register(Book)



class bmsAdmin(admin.ModelAdmin):
  list_display=['title','author','price','publisher']