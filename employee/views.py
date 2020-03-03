from django.shortcuts import render,HttpResponse
from .forms import *
from .models import *

# Create your views here.

def show(request):
    return render(request,'show.html')

def addDepartment(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)

        if form.is_valid():
            dep_name = request.POST.get('dep_name')
            depmodelobj = Department(name=dep_name)
            depmodelobj.save()

            return HttpResponse('<h3>Department is added successfully!!!</h3')

    else:
        form = DepartmentForm()

    return render(request, 'genericForm.html', {'form':form})



'''
def addProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project_name = request.POST.get('project_name')
            client_name = request.POST.get('client_name')
            contact_person = request.POST.get('contact_person')
            contact_person_email = request.POST.get('contact_person_email')

            proModelObj = Projects(project_name=project_name, client_name=client_name, contact_person=contact_person, contact_person_email=contact_person_email)
            proModelObj.save()

            return HttpResponse('<h3>project saved successfully!!</h3>')

    else:
        form = ProjectForm()
    return render(request, 'genericForm.html', {'form':form})
'''

def addProject(request):
    if request.method == "POST":
        form = ProjectModelForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponse("<h3>project is saved successfully!!</h3>")

    else:
        form = ProjectModelForm()

        return render(request, 'genericForm.html', { 'form' : form })

def addEmployee(request):
    if request.method == 'POST':
        form  = EmployeeForm(request.POST)

        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            empObj = Employee(first_name = first_name, last_name = last_name, email = email)
            empObj.save()

            department = request.POST.get('department')
            DepObj = Department.objects.get(id=department)

            designation = request.POST.get('designation')
            joining_date = request.POST.get('joining_date')
            birth_date =request.POST.get('birth_date')
            reveling_date = '9999-09-09'
            salary = request.POST.get('salary')
            total_experience =request.POST.get('total_experience')


            empDetObj = EmployeeDetails(employee = empObj, department = DepObj, designation = designation, joining_date = joining_date, 
            birth_date = birth_date, reveling_date=reveling_date, salary = salary, total_experience = total_experience)

            empDetObj.save()

            projects = request.POST.get('projects')
            proObj = Projects.objects.get(id=projects)

            empDetObj.projects.add(proObj)

            return HttpResponse("<h3>Employee data is saved successfully!</h3>")

    
    else:
        form = EmployeeForm()

        return render(request, 'genericForm.html', {'form' : form })

