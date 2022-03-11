from django.contrib import admin

from .models import Donation,Feedback
from .models import free_sessionform,internship


class Donor(admin.ModelAdmin):
    list_display = ['made_on','Name','Email','Amount','Mobileno']

class feedback(admin.ModelAdmin):
    list_display = ['made_on','Name','Query']

class Freesessionform(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile','field','doubt']

class internshipp(admin.ModelAdmin):
    list_display = ['made_on','name','email','mobile','field','cv']


admin.site.register(internship,internshipp)
admin.site.register(free_sessionform,Freesessionform)
admin.site.register(Donation,Donor)
admin.site.register(Feedback,feedback)
