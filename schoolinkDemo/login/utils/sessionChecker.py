from django.http import HttpResponseRedirect
from django.urls import reverse
from functools import wraps
from django.shortcuts import render
from django.shortcuts import redirect
#Using @wraps is better than manually overriding like doing wrap.__doc__ = fn.__doc__.

def myuser_login_required(f):
    @wraps(f)
    def wrap(request, *args, **kwargs):
        # if 'userId' not in request.session.keys():
        #     return  render(request, 'login.html')
        # else:
        #     return f(request, *args, **kwargs)
        if 'userId' in request.session.keys():
            return redirect('http://localhost:8000/user/dashboard')
        return f(request, *args, **kwargs)
    # wrap.__doc__=f.__doc__
    # wrap.__name__=f.__name__
    return wrap
