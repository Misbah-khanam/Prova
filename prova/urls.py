"""
URL configuration for prova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import *
from exam.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", register_user, name='register_user'),
    path("login/", login_user, name='login_user'),
    path("logout_view/", logout_view, name='logout_view'),
    path("upload_test/",upload_test,name="upload_test"),
    path("my_uploaded_tests/", my_uploaded_tests,name="my_uploaded_tests"),
    path("active_tests/", active_tests,name="active_tests"),
    path("my_ques/<int:exam_id>", my_ques,name="my_ques"),
    path("attempt_ques/<int:exam_id>", attempt_ques,name="attempt_ques"),
    path("attempted_tests/", attempted_tests,name="attempted_tests"),
    path("analytics_teacher/",analytics_teacher, name="analytics_teacher"),
    path("analytics_student/",analytics_student, name="analytics_student"),
    path("profile/",profile, name="profile")

]
