"""
URL configuration for EduPredict project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from EduPredict import auth

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('', auth.loginPage, name="login"),
    path('signup/', auth.SignupPage, name='signup'),
        path('signupinserted/', auth.signupPageinserted),
           path('loginresult/', auth.loginpage),



    path('forgot-password/', auth.forgotPasswordPage, name='forgot-password'),

    # Pages 
    path('home/', auth.homePage, name='home'), 
    path('about/', auth.aboutPage, name='about'),
    path('contact/', auth.contactPage, name='contact'),
]
