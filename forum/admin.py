from django.contrib import admin

from .models import Forum_table,Transaction,Donation,Mentor,Primemember,Feedback,solution
from .models import transcatid,course_info,hiring_mentor,coupon,free_sessionform,internship,Court


class forum_tab(admin.ModelAdmin):
    list_display = ['made_on','question','email','answer','answer_set']

class Donor(admin.ModelAdmin):
    list_display = ['made_on','Name','Email','Amount','Mobileno']

class mentor(admin.ModelAdmin):
    list_display = ['made_on','Name','Email','Mobileno','Profession','Mentor_Img']

class Transcation_data(admin.ModelAdmin):
    list_display = ['made_by','made_on','amount','order_id']

class prime(admin.ModelAdmin):
    list_display = ['made_on','Name','Email','Mobileno','Plan','Refered','Query']

class feedback(admin.ModelAdmin):
    list_display = ['made_on','Name','Query']

class imp(admin.ModelAdmin):
    list_display = ['made_on','order_id','transcation_id']

class Course_info(admin.ModelAdmin):
    list_display = ['made_on','name','mobile','email','Refered']

class hiring(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile','area']

class couponn(admin.ModelAdmin):
    list_display = ['made_on','email','mobile','finalcoupon']

class Freesessionform(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile','field','doubt']

class internshipp(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile','field','cv']

class court(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile','location']

class itsolution(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile']

admin.site.register(solution,itsolution)
admin.site.register(internship,internshipp)
admin.site.register(free_sessionform,Freesessionform)
admin.site.register(hiring_mentor,hiring)
admin.site.register(Forum_table,forum_tab)
admin.site.register(Donation,Donor)
admin.site.register(Mentor,mentor)
admin.site.register(Transaction,Transcation_data)
admin.site.register(Primemember,prime)
admin.site.register(Feedback,feedback)
admin.site.register(transcatid,imp)
admin.site.register(course_info,Course_info)
admin.site.register(coupon,couponn)
admin.site.register(Court,court)