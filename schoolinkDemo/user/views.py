from django.shortcuts import render, redirect, get_object_or_404
from user.utils.sessionChecker import sessionCheck
from .forms import * 
from user.models import *
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

@sessionCheck
def dashboard(request):
    return render(request, 'test1.html', {'hashedPassword' : request.session['fname']})



@sessionCheck
def createClass(request):
    try:
        if(request.method == 'POST'):
            if request.POST.get('csrfmiddlewaretoken') is not None:
                code = request.POST.get('code').strip()
                className = request.POST.get('name').strip()
                
                if(code is None):
                    return render(request, 'createClass.html', {'error' : 'code is required.'})
                if(className is None):
                    return render(request, 'createClass.html', {'error' : 'className is required.'})
                
                checkClassCodeExist = Classes.objects.filter(code=code).values()
                
                if(checkClassCodeExist.exists()):
                    return render(request, 'createClass.html', {'error' : 'Class code already exists.'}) 
                else:
                    # return render(request, 'class/createClass.html', {'error' : "IIIIII"})
                    # class = new Classes()
                    # class.code = code
                    # class.className = className
                    # class.isDelete = '0'
                    # class.save()
                    Classes.objects.create(code=code, className=className, isDelete='0')
                    return render(request, 'createClass.html', {'success' : 'Class created succesfully done.'})
            else:
              return render(request, 'createClass.html')  
        else:
            return render(request, 'createClass.html')
    except Exception as e:
        return render(request, 'createClass.html')



@sessionCheck
def listClass(request):
    try:
        classList = Classes.objects.filter(isDelete='0')
        paginator = Paginator(classList, 2)
        page = request.GET.get('page')
        classDetails = paginator.get_page(page)
        # return render(request, 'test1.html', {'hashedPassword': classDetails})
        return render(request, 'classList.html', {'classList': classDetails, 'number' : 1})
    except ValueError:
        raise Http404


@sessionCheck
def viewClass(request, class_id):
    try:
        classDetails = Classes.objects.filter(pk=class_id, isDelete='0').values()
        if(classDetails.exists()):
            return render(request, 'test1.html', {'hashedPassword' : classDetails})
        else:
            return redirect('http://localhost:8000/user/classList')
        # return render(request, 'test1.html', {'hashedPassword' : classDetails})
    except ValueError:
        raise Http404