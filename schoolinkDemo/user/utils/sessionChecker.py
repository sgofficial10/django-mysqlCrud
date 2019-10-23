from functools import wraps
from django.shortcuts import redirect

def sessionCheck(f):
    @wraps(f)
    def wrap(request, *args, **kwargs):
        if 'userId' not in request.session.keys():
            return redirect('http://localhost:8000/login')
        return f(request, *args, **kwargs)
    return wrap