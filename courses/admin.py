from django.contrib import admin
from . models import Teachers
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display =['name','sub_expart','profile_pic','date_of_joinig']

admin.site.register(Teachers,TeacherAdmin)
