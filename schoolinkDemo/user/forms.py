from django.forms import ModelForm 
from django import forms 
from user.models import *


class ClassesForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ["code", "className"]
    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function 
        super(ClassesForm, self).clean()

        # extract the username and text field from the data 
        classCode = self.cleaned_data.get('code') 
        className = self.cleaned_data.get('className')
        # conditions to be met for the username length 
        if len(classCode) < 5: 
            self._errors['classCode'] = self.error_class([ 
                'Minimum 5 characters required']) 
        if len(className) <10: 
            self._errors['className'] = self.error_class([ 
                'Post Should Contain minimum 10 characters']) 
        # return any errors if found 
        return self.cleaned_data 

