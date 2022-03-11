from django.db import models

class Donation(models.Model):
    Name = models.CharField(max_length=90,default="")
    Email = models.CharField(max_length=50,blank=True,default="")
    Amount = models.IntegerField(default=100)
    Date = models.DateTimeField(auto_now_add=True)
    Mobileno = models.CharField(max_length=100,default="",blank=True)
    made_on = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    Name = models.CharField(max_length=30,default="")
    Email = models.CharField(max_length=50,default="")
    Query = models.CharField(max_length=500,default="")
    made_on = models.DateTimeField(auto_now_add=True)

class free_sessionform(models.Model):
    email = models.CharField(max_length=30,default="",null=True)
    made_on = models.DateTimeField(auto_now_add=True)
    mobile = models.CharField(max_length=30,default="",null=True)
    name = models.CharField(max_length=30,default="",null=True)
    field = models.CharField(max_length=30,default="",null=True)
    doubt = models.CharField(max_length=300,default="",null=True)

class internship(models.Model):
    email = models.CharField(max_length=30,default="",null=True)
    made_on = models.DateTimeField(auto_now_add=True)
    mobile = models.CharField(max_length=30,default="",null=True)
    name = models.CharField(max_length=30,default="",null=True)
    field = models.CharField(max_length=30,default="",null=True)
    cv = models.FileField(blank=True, upload_to='cv')