from django.shortcuts import render, redirect, get_object_or_404
from user.utils.sessionChecker import sessionCheck
from .forms import * 
from user.models import *
from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from .forms import  ClassForm, SectionForm
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
#csrf_exempt is help to get POST data without csrf_token. It is a decorator @csrf_exempt

@sessionCheck
def dashboard(request):
    return render(request, 'dashboard.html')



@sessionCheck
def logout(request):
    del request.session['userType']
    del request.session['userId']
    del request.session['fname']
    return redirect('http://localhost:8000/login')

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
        classList = Classes.objects.get_query()
        paginator = Paginator(classList, 2)
        page = request.GET.get('page')
        classDetails = paginator.get_page(page)
        return render(request, 'classList.html', {'classList': classDetails, 'number' : 1})
    except ValueError:
        raise Http404


@sessionCheck
def viewClass(request, class_id):
    try:
        if class_id is not None:
            classDetails = Classes.objects.filter(pk=class_id, isDelete='0').values()
            if(classDetails.exists()):
                for classDetail in classDetails:
                    classDetail = classDetail
                if request.method == 'POST':
                    if(request.POST.get('csrfmiddlewaretoken')) is not None:
                        classname_exists = Classes.objects.filter(className=request.POST.get('name').strip()).exclude(pk=request.POST.get('classes_id')).values()
                        if classname_exists.exists():
                            return render(request, 'viewClass.html', {'classDetail' : classDetail, 'error' : 'Class name already exists in the system'})      
                        else:
                            updateClass = Classes.objects.get(pk=request.POST.get('classes_id'))
                            updateClass.className = request.POST.get('name').strip()
                            updateClass.save()
                            return redirect('/user/classList') 
                    else:
                        return render(request, 'viewClass.html', {'classDetail' : classDetail})
                else:
                    return render(request, 'viewClass.html', {'classDetail' : classDetail})
            else:
                return redirect('/user/classList')  
        else:
            return redirect('/user/classList')   
    except ValueError:
        return redirect('/user/classList')
    except:
        return redirect('/user/classList')  


@sessionCheck
# @csrf_exempt
def deleteClass(request):
    try:
        if request.method == 'POST':
            if request.POST.get('csrfmiddlewaretoken') is not None:
                class_id = request.POST.get('class_id')
                if class_id is None:
                    data = {
                        'error' : 'Class Id is required.'
                    }
                    return JsonResponse(data)
                else:
                    try:
                        class_exists = Classes.objects.get(pk=class_id)
                        # class_exists.isDelete = '1'
                        class_exists.delete()
                        data = {
                            'success' : 'successfully done.'
                        }
                        return JsonResponse(data)
                    except ObjectDoesNotExist:
                        data = {
                            'error' : 'Invalid class id.'
                        }
                        return JsonResponse(data)
            else:
                data = {
                    'error' : 'Invalid Action.'
                }
                return JsonResponse(data)
        else:
            data = {
                'error' : 'Invalid Method.'
            }
            return JsonResponse(data)
    except:
        data = {
            'error' : 'Unexcepted error ocurred.'
        }
        return JsonResponse(data)



@sessionCheck
def createSection(request):
    try:
        class_list = Classes.objects.get_query()
        class_list_count = Classes.objects.get_query().count()
        if(request.method == 'POST'):
            if request.POST.get('csrfmiddlewaretoken') is not None:
                sectionForm = SectionForm(request.POST)
                if sectionForm.is_valid():
                    Sections.objects.create(code=request.POST.get('code'), name=request.POST.get('name'), classes_id=request.POST.get('id'))
                    return render(request, 'section/createSection.html', {'classes_list' : class_list, 'class_list_count' : class_list_count, 'success' : 'Section created for given class succesfully done.'})
                else:
                    error = sectionForm.errors.get_json_data(escape_html=False).get('code')
                    for error_message in error:
                        error_message = error_message
                    return render(request, 'section/createSection.html', {'classes_list' : class_list, 'class_list_count' : class_list_count, 'error' : error_message.get('message')})    
            else:
                return render(request, 'section/createSection.html', {'classes_list' : class_list, 'class_list_count' : class_list_count})   
        else:
            return render(request, 'section/createSection.html', {'classes_list' : class_list, 'class_list_count' : class_list_count})
    except:
        raise Http404


@sessionCheck
def listSection(request):
    try:
        if request.method == 'POST':
            if request.POST.get('csrfmiddlewaretoken') is not None:
                class_id = request.POST.get('class_id', None)
                if class_id is None:
                    data = {
                        'error' : 'Class Id is required.'
                    }
                    return JsonResponse(data)
                else:
                    section_list = Sections.objects.filter(classes_id=class_id).values()
                    if section_list.exists():
                        data = { 'section_list' : list(section_list)}
                        return JsonResponse(data)
                    else:
                        data = { 'section_list' : ''} 
                        return JsonResponse(data) 
            else:
                data = {
                    'error' : 'Invalid Method.'
                }
                return JsonResponse(data) 
        else:
            data = {
                    'error' : 'Invalid Method.'
                }
        return JsonResponse(data)
    except:
        data = {
                'error' : 'Invalid Method.'
            }
        return JsonResponse(data)




@sessionCheck
def listSection(request):
    return render(request, 'test1.html', {'hashedPassword' : 'sffsfs'})



