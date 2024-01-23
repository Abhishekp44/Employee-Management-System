from django.shortcuts import render,redirect
from EMSapp.models import EmployeeManagement, DepartmentManagement, SalaryManagement
from EMSapp.forms import EmployeeForm,DepartmentForm,SalaryForm
from django.db.models import Sum

# Create your views here.
def home(request): 
    return render(request,'index.html')

def emp(request):
    e=EmployeeManagement.objects.all()
    context={}
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect('/emp')
    context['data']=e
    return render(request,'emp.html',context)

def dept(request):
    d=DepartmentManagement.objects.all()
    context={}
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect('/dept')
    context['data']=d
    return render(request,'dept.html',context)

def salary(request):
    d=SalaryManagement.objects.all()
    context={}
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect('/salary')
    context['data']=d
    return render(request,'salary.html',context)

def editemp(request,eid):
    e = EmployeeManagement.objects.filter(emp_id=eid)
    if not e.exists():
        return redirect('/emp')

    employee = e.first()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/emp')
    else:
        form = EmployeeForm(instance=employee)

    context = {'form': form}
    return render(request, 'editemp.html', context)

def delemp(request,eid):
    c=EmployeeManagement.objects.filter(emp_id=eid)
    c.delete()
    return redirect('/emp')

def editdept(request,eid):
    e = DepartmentManagement.objects.filter(dept_id=eid)
    if not e.exists():
        return redirect('/dept')

    Department = e.first()

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=Department)
        if form.is_valid():
            form.save()
            return redirect('/dept')
    else:
        form = DepartmentForm(instance=Department)

    context = {'form': form}
    return render(request, 'editdept.html', context)

def deldept(request,eid):
    c=DepartmentManagement.objects.filter(dept_id=eid)
    c.delete()
    return redirect('/dept')

def editsalary(request,eid):
    e = SalaryManagement.objects.filter(emp=eid)
    if not e.exists():
        return redirect('/salary')

    Department = e.first()

    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=Department)
        if form.is_valid():
            form.save()
            return redirect('/salary')
    else:
        form = SalaryForm(instance=Department)

    context = {'form': form}
    return render(request, 'editsalary.html', context)

def delsalary(request,eid):
    c=SalaryManagement.objects.filter(emp=eid)
    c.delete()
    return redirect('/salary')

def salaryrep(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')


        salaries = SalaryManagement.objects.filter(salary_date__range=[start_date, end_date])
        total_department_costs = salaries.values('dept__dept_name').annotate(total_cost=Sum('salary_amt'))

        context = {
            'start_date': start_date,
            'end_date': end_date,
            'total_department_costs': total_department_costs,
        }

        return render(request, 'salary_report.html', context)

    return render(request, 'salary_report.html', {})
