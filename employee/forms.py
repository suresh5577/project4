from django import forms
from .models import *

class DepartmentForm(forms.Form):
    dep_name = forms.CharField(label='department name', max_length=20)
''' 
class ProjectForm(forms.Form):
    project_name = forms.CharField(label='project name',max_length=20)
    client_name = forms.CharField(label='client name', max_length=20)
    contact_person = forms.CharField(label='contact person', max_length=20)
    contact_person_email = forms.CharField(label='contact person email', max_length=30)
    '''

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['project_name','client_name','contact_person','contact_person_email']


class EmployeeForm(forms.Form):
    first_name = forms.CharField(label='first name', max_length=10)
    last_name = forms.CharField(label='last name', max_length=10)
    email = forms.EmailField(label='email')
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    projects = forms.ModelChoiceField(queryset= Projects.objects.all())
    designation = forms.CharField(max_length=20)
    about_employee = forms.CharField(widget = forms.Textarea)
    joining_date = forms.DateField()
    birth_date = forms.DateField()
    #reveling_date = forms.DateField()
    salary = forms.IntegerField()
    total_experience = forms.FloatField()
