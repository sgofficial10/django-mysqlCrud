from django.forms import ModelForm 
from django import forms 
from .models import Classes, Sections
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

#clean_<fieldname is restricted for only one field>
#clean is userd for all field.

class SectionForm(forms.Form):
    code = forms.CharField(max_length=10)
    name = forms.CharField(max_length=10)
    id = forms.IntegerField()

    def clean_id(self):
        class_id = self.cleaned_data['id']
        class_id_exists = Classes.objects.filter(pk=class_id).values()
        if class_id_exists.exists():
            pass
        else:
            raise ValidationError('Invalid Class Id.')


    def clean_code(self):
        section_code = self.cleaned_data['code'].strip()
        section_code_exists = Sections.objects.filter(code=section_code).values()
        if section_code_exists.exists():
            raise ValidationError('Section code already exists.')

    def clean_name(self):
        section_name = self.cleaned_data.get('name' , None)
        if section_name is None:
            raise ValidationError('Section name is required.')
        else:
            pass
            # self.check_section_name_exists_for_class()

    # def check_section_name_exists_for_class(self):
    #     class_id = self.cleaned_data['id']
    #     section_name = self.cleaned_data.get('name')

    #     class_section_exists = Sections.objects.filter(classId=class_id, name_exact=section_name)
    #     if class_section_exists.exists():
    #         raise ValidationError('Section name alreadt exists for given class.')

