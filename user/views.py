from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.views import View

from user.user_request import get_user_request

User = get_user_model()


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        input_readings = get_user_request(request)
        
        user = User.objects.create(
            name = input_readings["name"],
            email = input_readings["email"],
            password = input_readings["password"],
            phone_number = input_readings["phone_number"],
            address = input_readings["address"],
            profile_picture = input_readings["profile_picture"],
        )
        
        user.set_password(input_readings["password"])
        user.save()
        
        return redirect("/login/")
            
            
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")
        
    def post(self, request):
        input_readings = get_user_request(request)
        
        email = input_readings["email"]
        password = input_readings["password"]
        
        if not User.objects.filter(email=email).exists():
            messages.error(request, "Invalid email")
            
            return redirect("/login/")
        
        user = authenticate(email=email, password=password)
        if user is None:
            messages.error(request, "Authentication Failed")
            
            return redirect("/login/")
        else:
            login(request, user)
            
            return redirect("/")
            
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        
        return redirect("/login/")
    
    
class DashboardView(View):
    def get(self, request):
        return render(request, "dashboard.html")
    
    
class UpdateUserView(View):
    def get(self, request):
        return render(request, "update_user.html")
        
    def post(self, request):
        user = request.user
        
        input_readings = get_user_request(request)
        
        fields_to_update = {
        "name":input_readings["name"],
        "phone_number":input_readings["phone_number"],
        "address":input_readings["address"],
        "profile_picture":input_readings["profile_picture"],
        } 

        for field, value in fields_to_update.items():
            if value:
                setattr(user, field, value)

        user.save()
        
        return redirect("/dashboard/")
      
   
class PasswordChangeView(View):
    def get(self, request):
        password_change_form = PasswordChangeForm(user=request)
        context = {"form":password_change_form}
        
        return render(request, "change_password.html", context)
    
    def post(self, request):
        change_password = PasswordChangeForm(user=request.user, data=request.POST)
        
        if change_password.is_valid():
            change_password.save()
            update_session_auth_hash(request, change_password.user)
            messages.success(request, "Password changed successfuly")
            
            return redirect("/dashboard/")
        else:
            messages.error(request, "Password failed!")
            
            return redirect("/change-password/")
        
