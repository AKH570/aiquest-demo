from django.contrib import admin
from . models import Expert,CourseList,AboutPage,Cart,Customer,Contact,ContactMsg

# Register your models here.
class ExpertAdmin(admin.ModelAdmin):
    list_display=['id','name','sub_expart','email','profile_pic','profile_details','date_of_joinig']
admin.site.register(Expert,ExpertAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display=['id','course_name','price','discount','description','teachers','prod_img']
admin.site.register(CourseList,CourseAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display=['title','descriptions','testmonial_text','title_img',]
admin.site.register(AboutPage,AboutAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']
admin.site.register(Cart,CartAdmin)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =['id', 'user', 'name','district','thana','villorroad','country','phone','zipcode']

#@admin.register(OrderPlaced)
#class OrderPlacedModelAdmin(admin.ModelAdmin):
 #   list_display = ['id', 'user', 'customer','product','quantity','ordered_date','status']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=['location','email','phone','subject']

@admin.register(ContactMsg)
class ContactMsgModelAdmin(admin.ModelAdmin):
    list_display=['name','email','course_name','message']