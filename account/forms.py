from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class account_creation_form(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control space'}))
    password2 = None
    class Meta:
        model = User
        fields = ['username','email']
        widgets = {'username':forms.TextInput(attrs = {'class':'form-control space'}),
                'email': forms.EmailInput(attrs = {'class':'form-control space'})}

class login_form(AuthenticationForm):
    username = forms.CharField(label = "Username",widget = forms.TextInput(attrs = {'class':'form-control space'}))
    password = forms.CharField(label="Password",widget = forms.PasswordInput(attrs = {'class':'form-control space'}))

class name_form(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class password_form(PasswordChangeForm):
    old_password = None
    new_password1 = forms.CharField(label="Newpassword",widget=forms.PasswordInput(attrs={'class':'form-control space'}))
    new_password2 = forms.CharField(label="Confirm Newpassword",widget=forms.PasswordInput(attrs={'class':'form-control space'}))
    class Meta:
        model = User

class user_change_form(UserChangeForm):
    password = None
    class Meta:
        model = User
        def __init__(self, *args, **kwargs):
            super(user_change_form, self).__init__(*args, **kwargs)
            instance = getattr(self, 'instance', None)
            if instance and instance.pk:
                self.fields['username'].widget.attrs['readonly'] = True

        fields = ['username','email','first_name','last_name',]
        widgets = {'username':forms.TextInput(attrs = {'class':'form-control space'}),
                'first_name':forms.TextInput(attrs = {'class':'form-control space'}),
                'last_name':forms.TextInput(attrs = {'class':'form-control space'}),
                'email':forms.EmailInput(attrs = {'class':'form-control space'}),
                }
        