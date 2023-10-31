from django.shortcuts import render, redirect
from user.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout

def register_user(request):
    messages = []
    if request.user.is_authenticated:
        if(request.user.user_type == "Teacher"):
            return redirect("my_uploaded_tests")
        if(request.user.user_type == "Student"):
            return redirect("active_tests")
    else:
        if request.method == 'POST':
            data = request.POST
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            password = make_password(f"{data.get('password')}")
            userType = data.get('user-type')
            create_user = User(name=name, email=email, phone=phone, user_type=userType, password=password)
            create_user.save()
            messages.append("user registered successfully")
            print(name, email, phone, password, userType)
            return render(request, "register.html",{"messages":messages})
    return render(request, "register.html")

def login_user(request):
    if request.user.is_authenticated:
        if(request.user.user_type == "Teacher"):
            return redirect("my_uploaded_tests")
        if(request.user.user_type == "Student"):
            return redirect("active_tests")
    else:
        if request.method == 'POST':
            data = request.POST
            email = data.get('email')
            password = data.get('password')
            userType = data.get('user-type')
            user = User.objects.filter(email=email).first()
            if(user):
                if(user.user_type == userType):
                    user_authenticate = authenticate(username=email, password=password)
                    if(user_authenticate):
                        login(request, user_authenticate)
                        print("user logged in successfully")
                        print(user.user_type)
                        if(user.user_type == "Teacher"):
                            return redirect("my_uploaded_tests")
                        if(user.user_type == "Student"):
                            return redirect("active_tests")
            else:
                print("invalid email or password")
            return render(request, "login.html")
        return render(request, "login.html")

def home(request):
    return render(request, "Home.html")


def logout_view(request):
    logout(request)
    return redirect('register_user')

def profile(request):
    return render(request, "profile.html")