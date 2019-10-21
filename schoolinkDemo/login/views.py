from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


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
                    hashedPassword = make_password(request.POST.get('password'))
                    return render(request, 'test.html', {'hashedPassword': hashedPassword})
                else:
                    return render(request, 'login.html')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    except:
        return render(request, 'login.html', {'error': 'something went wrong.'})
