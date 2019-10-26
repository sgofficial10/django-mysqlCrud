from django.shortcuts import render, redirect, get_object_or_404
from user.utils.sessionChecker import sessionCheck
from .forms import * 
from user.models import *
from django.core.paginator import Paginator
from django.http import Http404
from .forms import  ClassForm
from django.core.exceptions import ValidationError

@sessionCheck
def dashboard(request):
    return render(request, 'test1.html', {'hashedPassword' : request.session['fname']})



@sessionCheck
def createClass(request):
    try:
        if(request.method == 'POST'):
            # code = form.cleaned_data['title']
            if request.POST.get('csrfmiddlewaretoken') is not None:
                form = ClassForm(request.POST or None)
                if form.is_valid():
                    # class = new Classes()
                    # class.code = code
                    # class.className = className
                    # class.isDelete = '0'
                    # class.save()
                    Classes.objects.create(code=request.POST.get('code'), className=request.POST.get('name'), isDelete='0')
                    return render(request, 'createClass.html', {'success' : 'Class created succesfully done.'})
                else:
                    error = form.errors.get_json_data(escape_html=False).get('code')
                    for error_message in error:
                        error_message = error_message
                    return render(request, 'createClass.html', {'error' : error_message.get('message')})
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
        return render(request, 'classList.html', {'classList': classDetails, 'number' : 1})
    except ValueError:
        raise Http404


@sessionCheck
def viewClass(request, class_id):
    try:
        classDetails = Classes.objects.filter(pk=class_id, isDelete='0').values()
        if(classDetails.exists()):
            for classDetail in classDetails:
                classDetail = classDetail
            return render(request, 'viewClass.html', {'classDetail' : classDetail})
        else:
            return redirect('/user/classList')
    except ValueError:
        raise Http404

@sessionCheck
def updateClass(request):
    try:
        if(request.method == 'POST'):
            print(request.POST)
        else:
            return redirect('/user/classList')
    except:
        return redirect('/user/classList')
