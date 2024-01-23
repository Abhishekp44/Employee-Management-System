from django import forms
from EMSapp.models import EmployeeManagement,DepartmentManagement,SalaryManagement

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeManagement
        fields = ['emp_id','emp_name','emp_email','emp_address','hiring_date','salary','designation','reporting_manager']

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        # Set the size attribute for the text input fields
        self.fields['emp_id'].widget.attrs['size'] = 5
        self.fields['hiring_date'].widget.attrs['size'] = 5
        self.fields['salary'].widget.attrs['size'] = 5

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentManagement
        fields = ['empid','dept_id','dept_name','dept_floor']

class SalaryForm(forms.ModelForm):
    class Meta:
        model = SalaryManagement
        fields = ['emp','dept','salary_date','salary_amt','start_date','end_date']
