from .models import Forum,Mentor

from django import forms

class question_form(forms.ModelForm):
    class Meta:
        model=Forum
        fields=['question','email']
        widgets={'question':forms.Textarea(attrs={'rows':3,'cols':40,'class':'form-control'}),
            'email':forms.EmailInput(attrs={'rows':3,'cols':40,'class':'form-control'})}

class answer_form(forms.ModelForm):
    class Meta:
        model=Forum
        fields=['answer']
        widgets={'answer':forms.Textarea(attrs={'rows':3,'cols':40,'class':'form-control'})}

class volunter_form(forms.ModelForm):
    class Meta:
        model=Mentor
        fields=['Name','Mobileno','Email','Profession','Mentor_Img']
        widgets={'Name':forms.TextInput(attrs={'class':'form-control space'}),
                'Mobileno':forms.TextInput(attrs={'class':'form-control space'}),
                'Email':forms.EmailInput(attrs={'class':'form-control space'}),
                'Profession':forms.TextInput(attrs={'class':'form-control space'}),
                'Mentor_Img':forms.FileInput(attrs={'class':'form-control space'})
                }