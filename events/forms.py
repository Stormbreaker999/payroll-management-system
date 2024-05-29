from django import forms, template
from django.forms import ModelForm
from .models import Department, Employee, Bank_Details

#Create a Department Form
class DepartmentForm(ModelForm):
    class Meta:
        model=Department
        lis=Department.objects.all()
    
        fields="__all__"#"__all__" for all fields

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=('ID', 'Name', 'DOB', 'Address', 'Contact', 'Email', 'Dept', 'Job_code', 'Salary', 'DOJ')

        widgets={
            'ID': forms.NumberInput(attrs={'class': 'form-control col-md-4'}),
            
            'Name': forms.TextInput(attrs={'class':'form-control col-md-4'}),
            'DOB': forms.NumberInput(attrs={'class':'form-control col-md-4', 'type':'date'}),
            'Address': forms.TextInput(attrs={'class':'form-control col-md-4'}),
            'Contact': forms.NumberInput(attrs={'class':'form-control col-md-4'}),
            'Email': forms.EmailInput(attrs={'class':'form-control col-md-4'}),
            'Dept': forms.Select(attrs={'class':'form-control col-md-4'}),
            'Job_code': forms.Select(attrs={'class':'form-control col-md-4'}),
            'Salary': forms.NumberInput(attrs={'class':'form-control col-md-4'}),
            'DOJ': forms.NumberInput(attrs={'class':'form-control col-md-4', 'type':'date'}),
        }
        labels={
            'ID':'Employee ID :',
            'Name': 'Employee Name :',
            'DOB': 'Date of Birth :',
            'Address':'Address :',
            'Contact':'Contact No. :',
            'Email': 'Email ID',
            'Dept': 'Department Name',
            'Job_Code': 'Job Code',
            'DOJ': 'Date of Joining',
            'Salary': 'Total Salary'
        }

class view_dep_form(ModelForm):
    class Meta:
        model=Department
        fields=('Dep_Name',)
    widgets={
        'Dep_Name':forms.Select(attrs={'class':'form-control'}),
    }

class bank(ModelForm):
    class Meta:
        model=Bank_Details
        fields=('Bank_Name', 'IFSC', 'Accno')
        