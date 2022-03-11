from django import forms
from .models import Feedback

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