
from .models import Forum_table,Mentor,Feedback
from django import forms


class feedbackform(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['Name','Email','Query']
        widgets={'Name':forms.TextInput(attrs={'class':'form-control'}),
                'Email':forms.TextInput(attrs={'class':'form-control'}),
                 'Query':forms.Textarea(attrs={'class':'form-control'})}

class question_form(forms.ModelForm):
    class Meta:
        model=Forum_table
        fields=['question','email']
        widgets={'question':forms.Textarea(attrs={'rows':3,'cols':40,'class':'form-control'}),
            'email':forms.EmailInput(attrs={'rows':3,'cols':40,'class':'form-control'})}

class answer_form(forms.ModelForm):
    class Meta:
        model=Forum_table
        fields=['answer']
        widgets={'answer':forms.Textarea(attrs={'rows':3,'cols':40,'class':'form-control'})}


class volunter_form(forms.ModelForm):
    class Meta:
        model=Mentor
        fields=['Name','Mobileno','Email','Profession','Mentor_Img']
        widgets={'Name':forms.TextInput(attrs={'class':'form-control'}),
                'Mobileno':forms.TextInput(attrs={'class':'form-control'}),
                'Email':forms.EmailInput(attrs={'class':'form-control'}),
                'Profession':forms.TextInput(attrs={'class':'form-control'})
                }

class digitalform(forms.Form):
    Name=forms.CharField(label="username",widget=forms.TextInput(attrs={'class':'form-control'}))
    Email=forms.CharField(label="email",widget=forms.TextInput(attrs={'class':'form-control'}))
    Mobileno=forms.CharField(label="mobile",widget=forms.TextInput(attrs={'class':'form-control'}))