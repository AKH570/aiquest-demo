from django.contrib import admin
from . models import Expert,CourseList

# Register your models here.
class ExpertAdmin(admin.ModelAdmin):
    list_display=['name','sub_expart','email','profile_pic','profile_details','date_of_joinig']
admin.site.register(Expert,ExpertAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display=['course_name','price','discount','description','teachers','prod_img']
admin.site.register(CourseList,CourseAdmin)
