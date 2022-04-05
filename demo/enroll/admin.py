from django.contrib import admin

from enroll.models import Employee, Student


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('empid','empname','empemail')

# Register your models here.
admin.site.register(Student)
# admin.site.register(Employee,EmployeeAdmin)