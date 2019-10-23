from django.shortcuts import render
from user.utils.sessionChecker import sessionCheck
# Create your views here.

@sessionCheck
def dashboard(request):
    return render(request, 'test1.html', {'hashedPassword' : request.session['fname']})

