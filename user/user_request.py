def get_user_request(request):
    user_input = {
        "name":request.POST.get("name"),
        "email":request.POST.get("email"),
        "password":request.POST.get("password"),
        "phone_number":request.POST.get("phone_number"),
        "address":request.POST.get("address"),
        "profile_picture":request.FILES.get("profile_picture")
    }
    
    return user_input

