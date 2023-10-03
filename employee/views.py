from django.shortcuts import render, redirect
from .models import Employee

def index(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'index.html', context)


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        designation = request.POST.get('designation')

        Employee.objects.create(
            name=name,
            email=email,
            address=address,
            designation=designation
        )
    return redirect('index')


def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        designation = request.POST.get('designation')

        emp = Employee(
            id=id,
            name=name,
            email=email,
            address=address,
            designation=designation
        )
        emp.save()
    return redirect('index')


def delete(request, id):
    Employee.objects.filter(id=id).delete()
    return redirect('index')