from django.db import models

# Create your models here.
class Job(models.Model):
    Code=models.IntegerField('JobId', primary_key=True)
    Post=models.CharField('Job Post', max_length=20, null=False)
    HRA=models.IntegerField('HRA', null=False)
    TA=models.IntegerField('TA')
    DA=models.IntegerField('DA')
    PF=models.IntegerField('PF')
    IT=models.IntegerField('IT')
    def __str__(self):
        return "Grade " + str(self.Code)
class Department(models.Model):
    Dep_ID=models.CharField('Department_ID', max_length=5, primary_key=True)
    Dep_Name=models.CharField('Department_Name', unique=True, max_length=20, null=False)
    Manager=models.CharField("Manager_Name", max_length=40, null=False)

    def __str__(self):
        return self.Dep_Name
class Employee(models.Model):
    ID=models.IntegerField('ID', primary_key=True)
    Name=models.CharField('Name', max_length=35, null=False)
    DOB=models.DateField('Date_of_Birth', null=False)
    
    Address=models.CharField('Address', max_length=60, null=False)
    Contact=models.BigIntegerField('Contact_No', null=False)
    Email=models.EmailField('Email_id', null=False)
    Dept=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    Job_code=models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    Salary=models.IntegerField('Total Salary', null=False)
    DOJ=models.DateField('Date_Of_Joining', null=False)
    def __str__(self):
        return str(self.ID)
class Transactions(models.Model):
    Sno=models.IntegerField('S.No.', primary_key=True)
    ID=models.ForeignKey(Employee, on_delete=models.SET_NULL,null=True)
    DID=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    Attendance=models.IntegerField('Attendance')
    PDate=models.DateField('Payment Date')
    Salary=models.IntegerField('Total Salary')
    HRA=models.IntegerField('HRA')
    TA=models.IntegerField('TA')
    DA=models.IntegerField('DA')
    PF=models.IntegerField('PF')
    IT=models.IntegerField('IT')
class Bank_Details(models.Model):
    ID=models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    Accno=models.BigIntegerField('Account No', null=False)
    IFSC=models.CharField('IFSC Code', max_length=12)
    Bank_Name=models.CharField('Bank Name', max_length=30, default='NULL')

class PFReport(models.Model):
    Sno=models.IntegerField('Sno', primary_key=True)
    Accno=models.IntegerField('Account No', null=False)
    IFSC=models.CharField('IFSC Code', max_length=12)
    Bank_Name=models.CharField('Bank Name', max_length=30)
    PFAmount=models.IntegerField('PFAmount')
    Date=models.DateField('Date')
