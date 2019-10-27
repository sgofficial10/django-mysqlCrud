from django.forms import ModelForm 
from django import forms 
from .models import Classes
from django.core.exceptions import ValidationError


# class ClassFormModel(forms.ModelForm):
#     class Meta:
#         model = Classes
#         fields = ['code', 'className']
        


class ClassForm(forms.Form):
    code = forms.CharField(max_length=10)
    name = forms.CharField(max_length=10)
    # email = forms.EmailField()
    # content = forms.CharField(widget=forms.Textarea)

    def clean_code(self):
        code = self.cleaned_data['code'].strip()
        if code is None:
            raise ValidationError('Class code is required.')
        else:
            class_code_exists = Classes.objects.filter(code=code).values()
            if class_code_exists.exists():
                raise ValidationError('Class code already exists.')

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if name is None:
           raise ValidationError('class name is required.') 
        else:
            class_name_exists = Classes.objects.filter(className = name).value()
            if class_name_exists.exists():
                raise ValidationError('Class name already exists.')

