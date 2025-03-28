from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import Booking

class RegisterForm(forms.ModelForm):
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username'}),
        label='Username',
        help_text=None,
    )
    
    email = forms.EmailField( 
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email: Example@gmail.com'}),
        label='Email',
        help_text=None,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'enter password'}),
        label='Enter Password',
        help_text=None,
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),  
        label='Confirm Password',
        help_text=None,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password'] 

   



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'username',
            'required': True
        })
    )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'password',
            'required': True
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})

class ResetPasswordForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'True'
        })


class ResetPasswordConfirmForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(ResetPasswordConfirmForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'New Password',
            'required': 'True'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Retype New Password',
            'required': 'True'
        })
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''
        

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date_time', 'contact_infor', 'service_selection', 'location_infor', 'additional_details']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'contact_infor': forms.TextInput(attrs={'placeholder': 'Contact Information'}),
            'location_infor': forms.TextInput(attrs={'placeholder': 'Location'}),
            'additional_details': forms.Textarea(attrs={'placeholder': 'Additional Details', 'rows': 3}),
        }