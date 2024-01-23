from django.contrib import admin
from EMSapp.models import EmployeeManagement, DepartmentManagement, SalaryManagement

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['emp_id','emp_name','emp_email','emp_address','hiring_date','salary', 'designation','reporting_manager']
    list_filter=['designation']

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['empid','dept_id','dept_name','dept_floor']
    list_filter=['dept_name']
# Register your models here.
admin.site.register(EmployeeManagement,EmployeeAdmin)
admin.site.register(DepartmentManagement,DepartmentAdmin)
admin.site.register(SalaryManagement)