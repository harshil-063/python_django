from django.contrib import admin

from .models import Student, teacher


# Register your models here.
@admin.register(Student)
class studentadmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city','marks','pass_date']


@admin.register(teacher)
class teacheradmin(admin.ModelAdmin):
    list_display = ['id','name','empnum','city','salary','join_date']