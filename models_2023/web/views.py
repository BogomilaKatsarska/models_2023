from django.shortcuts import render, get_object_or_404, redirect

from models_2023.web.models import Employee


def index(request):
    # x = list(Employee.objects.all())
    # employees_aged_35 = Employee.objects.filter(age=35)
    # employees_not_aged_35 = Employee.objects.exclude(age=35)
    # employee_with_id_1 = Employee.objects.get(id=1) --> 'GET' returns a single object, not a QuerySet
    # pass
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'index.html', context)


def delete_employee(request, pk):
    department_pk = 3
    Employee.objects.filter(department_id=department_pk).delete()
    # employee = get_object_or_404(Employee, pk=pk)
    # employee.delete()
    return redirect('index')