from django.contrib import admin

from .models import Donation,Feedback
from .models import Freesession,Internship


class Donor(admin.ModelAdmin):
    list_display = ['made_on','Name','Email','Amount','Mobileno']

class feedback(admin.ModelAdmin):
    list_display = ['made_on','Name','Query']

class Freesessionform(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile','field','doubt']

class internshipp(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile','field','checkbox1','checkbox2','cv']


admin.site.register(Internship,internshipp)
admin.site.register(Freesession,Freesessionform)
admin.site.register(Donation,Donor)
admin.site.register(Feedback,feedback)
