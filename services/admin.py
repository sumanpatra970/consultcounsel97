from django.contrib import admin
from .models import Forum,Transaction,Mentor,Primemember,Solution
from .models import Transcatid,Course,Court,Hirementor

class forum_tab(admin.ModelAdmin):
    list_display = ['made_on','question','email','answer','answer_set']

class mentor(admin.ModelAdmin):
    list_display = ['made_on','Name','Email','Mobileno','Profession','Mentor_Img']

class Transcation_data(admin.ModelAdmin):
    list_display = ['made_on','made_by','amount','order_id']

class prime(admin.ModelAdmin):
    list_display = ['made_on','Name','Email','Mobileno','Plan','Refered','Query']

class Course_info(admin.ModelAdmin):
    list_display = ['made_on','name','mobile','email','Refered']

class hiring(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile','area']

class court(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile','location']

class itsolution(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile']

class imp(admin.ModelAdmin):
    list_display = ['made_on','order_id','transcation_id']

admin.site.register(Transcatid,imp)
admin.site.register(Court,court)
admin.site.register(Course,Course_info)
admin.site.register(Mentor,mentor)
admin.site.register(Transaction,Transcation_data)
admin.site.register(Primemember,prime)
admin.site.register(Hirementor,hiring)
admin.site.register(Forum,forum_tab)
admin.site.register(Solution,itsolution)