from datetime import datetime
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = request.POST['phone']
        dept = request.POST['department']
        role = request.POST['role']
        location = request.POST['location']
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_name=dept, role_name=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully!')
    elif request.method == "GET":
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('An Exception Occured, Employee not added!')

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            employee_remove = Employee.objects.get(id=emp_id)
            employee_remove.delete()
            return HttpResponse('Employee Removed Successfully!')
        except:
            return HttpResponse('Please Enter Vslid EMP ID.')
    
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['department']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps' : emps
        }

        return render(request, 'view_all_emp.html', context)

    elif request.method == "GET":
        return render(request, 'filter_emp.html')

    else:
        return HttpResponse('An Exception Occured')

    return render(request, 'filter_emp.html')
