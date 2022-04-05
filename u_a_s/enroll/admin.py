from django.contrib import admin

from .models import blog

# Register your models here.

@admin.register(blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title','desc']

