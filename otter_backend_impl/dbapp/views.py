from django.shortcuts import render
from .models import Employee

def testmysql(request):
    employees = Employee.objects.all()
    context = {
        'user_ssn': employees[0].ssn if employees else 'N/A',
        'user_name': employees[0].lname if employees else 'N/A',
    }
    return render(request, 'home.html', context)