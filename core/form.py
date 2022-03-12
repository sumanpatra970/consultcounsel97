from django import forms
from .models import Feedback

from django.core.validators import FileExtensionValidator

class feedbackform(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['Name','Email','Query']
        widgets={'Name':forms.TextInput(attrs={'class':'form-control space'}),
                'Email':forms.TextInput(attrs={'class':'form-control space'}),
                 'Query':forms.Textarea(attrs={'class':'form-control space'})}


class digitalform(forms.Form):
    Name=forms.CharField(label="Name",widget=forms.TextInput(attrs={'class':'form-control sapce'}))
    Email=forms.CharField(label="Email",widget=forms.TextInput(attrs={'class':'form-control space'}))
    Mobileno=forms.CharField(label="Mobile",widget=forms.TextInput(attrs={'class':'form-control space'}))

class internform(forms.Form):
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control space'}))
    Mobile=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control space'}))
    Email=forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control space'}))
    Degree=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control space'}))
    resume=forms.FileField(label='Upload cv',widget=forms.FileInput(attrs={'class':'form-control space'}))
