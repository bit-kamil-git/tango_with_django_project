from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')   # display title, category, and url fields in admin interface

# Register your models here.
admin.site.register(Category)              # register Category model
admin.site.register(Page, PageAdmin)                  # register Page model
