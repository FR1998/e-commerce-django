from django import forms
from django.contrib.auth.password_validation import validate_password


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
    
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

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

