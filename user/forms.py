from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    profile_picture = forms.ImageField()
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        
        return password
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists!")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Phone number must be unique!")
        return phone_number
    
    def clean(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )  


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UpdateForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(required=False)

