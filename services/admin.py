from django.contrib import admin

from .models import Forum_table,Transaction,Mentor,Primemember,solution
from .models import transcatid,course_info,hiring_mentor,Court
class forum_tab(admin.ModelAdmin):
    list_display = ['made_on','question','email','answer','answer_set']

class mentor(admin.ModelAdmin):
    list_display = ['made_on','Name','Email','Mobileno','Profession','Mentor_Img']

class Transcation_data(admin.ModelAdmin):
    list_display = ['made_by','made_on','amount','order_id']

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

admin.site.register(transcatid,imp)
admin.site.register(Court,court)
admin.site.register(course_info,Course_info)
admin.site.register(Mentor,mentor)
admin.site.register(Transaction,Transcation_data)
admin.site.register(Primemember,prime)
admin.site.register(hiring_mentor,hiring)
admin.site.register(Forum_table,forum_tab)
admin.site.register(solution,itsolution)