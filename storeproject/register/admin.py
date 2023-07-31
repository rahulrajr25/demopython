from django.contrib import admin

from register.models import CV, Course, Department,Purpose

# Register your models here.
admin.site.register(CV)


admin.site.register(Purpose)
admin.site.register(Department)
admin.site.register(Course)