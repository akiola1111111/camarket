from django.contrib import admin

from .models import Category, Item

admin.site.register(Category)
admin.site.register(Item)

admin.site.site_header = "admin akiola"
admin.site.site_title = "admin akiola"
admin.site.index_title = "admin akiola"
