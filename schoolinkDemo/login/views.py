from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from login.models import User
from login.utils.sessionChecker import myuser_login_required
from user.views import *
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

@myuser_login_required
def index(request):
    try:
        if(request.method == 'POST' ):
            if(request.POST.get('csrfmiddlewaretoken') is not None):
                if(request.POST.get('Login') == 'Login'):
                    email = request.POST.get('email').strip()
                    password = request.POST.get('password').strip()
                    if(email is None):
                        return render(request, 'login.html', {'error' : 'Email is required.'})
                    if(password is None):
                        return render(request, 'login.html', {'error' : 'Password is required.'})
                    # hashedPassword = make_password(request.POST.get('password'))
                    getUserDetails = User.objects.filter(email=email).values()
                    if(getUserDetails.exists()):
                        for getUserDetail in getUserDetails:
                            getUserDetail = getUserDetail
                        if(check_password(request.POST.get('password'), getUserDetail.get('password'))):
                            if(getUserDetail.get('active') == 1):
                                if(getUserDetail.get('userType') == '1'):
                                    userType = 'admin'
                                elif getUserDetail.get('userType') == '2':
                                    userType = 'Teacher'
                                elif getUserDetail.get('userType') == '3':
                                    userType = 'Parent'
                                else:
                                    userType = 'Driver'
                                #set session
                                request.session['userType'] = userType
                                request.session['userId'] = getUserDetail.get('id')
                                request.session['fname'] = getUserDetail.get('fname')
                                return redirect('http://localhost:8000/user/dashboard/')
                                # return render(request, 'test.html', {'hashedPassword' : request.session['fname']})
                            else:
                               return render(request, 'login.html', {'error': 'User is not active.Please contact to admin.'}) 
                        else:
                            return render(request, 'login.html', {'error': 'Invalid Password.'})
                    else:
                        return render(request, 'login.html', {'error': 'Invalid Credentials.'})
                else:
                    return render(request, 'login.html')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    except Exception as e:
        return render(request, 'login.html', {'error': 'something went wrong.'})
