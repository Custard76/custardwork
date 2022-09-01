from unicodedata import name
from django.contrib import admin
from .models import Contact
from .models import Images

# Register your models here.

class Comment (admin.ModelAdmin):
    admin.site.site_header = "Kitan Cleaning"
    admin.site.site_title = "Cleaning service"
    admin.site.index_title= "Cleaning service"
    list_display = ("name", "email", "phon`e", "message")
    list_editable = ("email", "phone")


class Image_comment (admin.ModelAdmin):
    list_display = ('image',)    


admin.site.register(Contact,Comment)
admin.site.register(Images,Image_comment)