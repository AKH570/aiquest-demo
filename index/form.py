from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from . models import Customer,ContactMsg

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model =User
        fields=['username','email','password1','password2']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
    
class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


#Profile
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','district','thana','villorroad','country','phone','zipcode']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'district':forms.TextInput(attrs={'class':'form-control'}), 'thana':forms.TextInput(attrs={'class':'form-control'}),'villorroad':forms.TextInput(attrs={'class':'form-control'}),'country':forms.TextInput(attrs={'class':'form-control'}),'phone':forms.TextInput(attrs={'class':'form-control'}),'zipcode':forms.NumberInput(attrs={'class':'form-control'})}

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMsg
        fields = ['name','email','course_name','message']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}), 'course_name':forms.TextInput(attrs={'class':'form-control'}), 'message':forms.Textarea(attrs={'class':'form-control'})}