from django.contrib import admin
from .models import Department, Course


#
#
# # Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['departmentname']


admin.site.register(Department, DepartmentAdmin)


#
#
class CourseAdmin(admin.ModelAdmin):
    list_display = ['deptid', 'crsename']
    prepopulated_fields = {'crsename': ('deptid',)}


admin.site.register(Course, CourseAdmin)
