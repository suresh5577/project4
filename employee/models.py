from django.db import models
from datetime import date

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return " %s %s " % (self.first_name, self.last_name)


class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Projects(models.Model):
    project_name = models.CharField(max_length=20)
    client_name = models.CharField(max_length=10)
    contact_person = models.CharField(max_length=20)
    contact_person_email = models.EmailField()

    def __str__(self):
        return "%s %s" %(self.project_name, self.client_name)

class EmployeeDetails(models.Model):
    employee =  models.ForeignKey(Employee, default=1, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    designation = models.CharField(max_length=25)
    about_employee = models.TextField()
    joining_date = models.DateField()
    birth_date = models.DateField()
    reveling_date = models.DateField()
    projects = models.ManyToManyField(Projects)
    salary = models.IntegerField()
    total_experience = models.FloatField()

    def __str__(self):
        return " %s %s " %(self.department,self.designation)

   








