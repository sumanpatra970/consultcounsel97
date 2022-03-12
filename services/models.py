from django.db import models

class Forum(models.Model):
    question = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100,default="")
    answer = models.TextField(max_length=2000,blank=True)
    answer_set = models.TextField(max_length=2000,default="",blank=True)
    made_on = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    made_by = models.CharField(max_length=100)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=100)
    order_id = models.CharField(unique=False, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

class Mentor(models.Model):
    Name = models.CharField(max_length=100,default="",blank=False)
    Mobileno = models.CharField(max_length=100,blank=False,default="")
    Email = models.CharField(max_length=100,blank=False,default="")
    Profession = models.CharField(max_length=200,default="",blank=True)
    Mentor_Img = models.ImageField(upload_to='',default="",blank=True)
    made_on = models.DateTimeField(auto_now_add=True)

class Primemember(models.Model):
    Name = models.CharField(max_length=50,blank=False)
    Email = models.CharField(max_length=50,blank=False)
    Mobileno = models.CharField(max_length=50,blank=False)
    Refered = models.CharField(max_length=20,default="",blank=False)
    Plan = models.CharField(max_length=20,default="")
    Query = models.CharField(max_length=100,blank=False,default="")
    made_on = models.DateTimeField(auto_now_add=True)

class Transcatid(models.Model):
    made_on = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    transcation_id = models.CharField(unique=True, max_length=100, null=True, blank=True)

class Course(models.Model):
    name = models.CharField(max_length=30,default="",null=True)
    made_on = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=30,default="",null=False)
    mobile = models.CharField(max_length=30,default="",null=False)
    Refered = models.CharField(max_length=20,default="NA",null=True)

class Hirementor(models.Model):
    name = models.CharField(max_length=30,default="",null=True)
    made_on = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=30,default="",null=True)
    mobile = models.CharField(max_length=30,default="",null=True)
    area = models.CharField(max_length=20,default="",null=True)

class Court(models.Model):
    email = models.CharField(max_length=30,default="",null=True)
    made_on = models.DateTimeField(auto_now_add=True)
    mobile = models.CharField(max_length=30,default="",null=True)
    name = models.CharField(max_length=300,default="",null=True)
    location = models.CharField(max_length=300,default="",null=True)

class Solution(models.Model):
    email = models.CharField(max_length=30,default="",null=True)
    made_on = models.DateTimeField(auto_now_add=True)
    mobile = models.CharField(max_length=30,default="",null=True)
    name = models.CharField(max_length=300,default="",null=True)