from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.views import View

from user.forms import *

User = get_user_model()
#Django forms added

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        
        context = {"form":register_form}
        
        return render(request, "register.html", context)
    
    def post(self, request):
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            
            user = User.objects.create(
                name=register_form.cleaned_data["name"],
                email=register_form.cleaned_data["email"],
                phone_number=register_form.cleaned_data["phone_number"],
                address=register_form.cleaned_data["address"],
                profile_picture=register_form.cleaned_data["profile_picture"],
            )
            user.set_password(register_form.cleaned_data["password"])
            user.save()
            return redirect("/login/")
        
        return render(request, "register.html", {"form":register_form})
        
                        
class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        
        context = {"form":login_form}
        
        return render(request, "login.html", context)
    
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            
            email=login_form.cleaned_data["email"]
            password=login_form.cleaned_data["password"]
            
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)

                return redirect("/")
            else:
                login_form.add_error(None,"Invalid email or password.")

        return render(request, "login.html", {"form": login_form})
            
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        
        return redirect("/login/")
    
    
class UpdateUserView(View):
    def get(self, request):
        user = request.user
        
        update_form = UpdateForm(initial={
            "name": user.name,
            "phone_number": user.phone_number,
            "address": user.address,
            })
        
        context = {"form": update_form}
        
        return render(request, "update_user.html", context)
    
    
    def post(self, request):
        update_form = UpdateForm(request.POST, request.FILES)
        if update_form.is_valid():
            user = request.user
            
            user.name = update_form.cleaned_data["name"]
            user.phone_number = update_form.cleaned_data["phone_number"]
            user.address = update_form.cleaned_data["address"]
            profile_picture = update_form.cleaned_data["profile_picture"]

            if profile_picture:
                user.profile_picture = profile_picture

            user.save()
            return redirect("/")
        
        return render(request, "update_user.html", {"form": update_form})
      
   
class PasswordChangeView(View):
    def get(self, request):
        password_change_form = PasswordChangeForm(user=request.user)
        
        context = {"form":password_change_form}
        
        return render(request, "change_password.html", context)
    
    def post(self, request):
        change_password_form = PasswordChangeForm(user=request.user, data=request.POST)
        
        if change_password_form.is_valid():
            change_password_form.save()
            update_session_auth_hash(request, change_password_form.user)
            messages.success(request, "Password changed successfuly")
            
            return redirect("/dashboard/")
        else:
            messages.error(request, "Password failed!")
            
            return redirect("/change-password/")
        
