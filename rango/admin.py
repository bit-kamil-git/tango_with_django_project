from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')   # display title, category, and url fields in admin interface

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}     # prepopulate slug field with name field


# Register your models here.
admin.site.register(Category, CategoryAdmin)              # register Category model
admin.site.register(Page, PageAdmin)                  # register Page model
