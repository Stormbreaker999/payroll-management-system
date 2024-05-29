from django.shortcuts import render
from .forms import DepartmentForm, EmployeeForm, bank
from django.http import HttpResponseRedirect
from .models import Department, Employee, Job, Transactions, PFReport, Bank_Details
from datetime import datetime
from django.db.models import Max, Sum
import calendar
# Create your views here.
def home(request):

    return render(request, 'home.html', {"name":"Avichal"})
def new_dep(request):
    submitted=False
    if request.method=="POST":
        form=DepartmentForm(request.POST)
        print(form)
        if (form.is_valid()):
            print("Here")
            form.save()
            return HttpResponseRedirect('/new_dep?submitted=True')
    else:
        form=DepartmentForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'new_dep.html', {'form':form, 'submitted':submitted})
def new_emp(request):
    submitted=False
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if (form.is_valid()):
            print("Here")
            form.save()
            return HttpResponseRedirect('/new_emp?submitted=True')
    else:
        form=EmployeeForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'new_emp.html', {'form':form, 'submitted':submitted})
    

def view_dep(request):
    if request.method=="POST":
        dep_list=Department.objects.values_list('Dep_Name')
        dep_list=[val[0] for val in dep_list]
        de=request.POST['dep']
        dep_det=Department.objects.values()
        dep_det=dep_det.filter(Dep_Name__startswith=de)
        dep_det=list(dep_det)
        dep_det=dep_det[0]
        emp_det=Employee.objects.values('ID', 'Name', 'Contact', 'Job_code_id', 'Dept', 'DOB', 'Email', 'Address').filter(Dept=dep_det['Dep_ID'])
        emp_det=list(emp_det)
        
        flag=1
        return render(request, 'view_dep.html', {'form':flag, 'dep_det':dep_det, 'dep_list':dep_list, 'emp_det':emp_det})
    else:
        dep_list=Department.objects.values_list('Dep_Name')
        dep_list=[val[0] for val in dep_list]
        flag=0
        return render(request, 'view_dep.html', {'form':flag, 'dep_list':dep_list})
def view_emp(request):
    dep_list=Department.objects.values_list('Dep_Name')
    dep_list=[val[0] for val in dep_list]
    if request.method=="POST":
        dep=request.POST['dep']
        dep_det=Department.objects.filter(Dep_Name__startswith=dep)
        dep_det=dep_det.values()
        dep_det=list(dep_det)[0]
        dep_name=dep_det['Dep_Name']
        dep=dep_det['Dep_ID']
        ID=request.POST['ID']
        try:
            ID=int(ID)
        except:
            return render(request, 'view_emp.html', {'form':0})
        data=Employee.objects.filter(Dept=dep)
        data=data.filter(ID=ID)
        data=data.values()
        data=list(data)[0]
        flag=1
        return render(request, 'view_emp.html', {'form':flag, 'dep_list':dep_list, 'data':data, 'dep_name':dep_name})
    else:
        
        flag=0
        return render(request, 'view_emp.html', {'form':flag, 'dep_list':dep_list})
    
def issue_salary(request):
    dep_list=Department.objects.values_list('Dep_Name')
    dep_list=[val for val in dep_list]
    if request.method=="GET":
        success=True
        flag =1
        try: 
            eid=request.GET['EID']
        except:
            flag=0
            return render(request, 'issue_salary.html', {'flag':flag, 'dep_list':dep_list, 'success:':success})
        
        eid=int(request.GET['EID'])
        mon=request.GET['mon'][5:]
        att=int(request.GET['Attendance'])
        print(eid, mon, att)
        emp=Employee.objects.filter(ID=eid)
        
        emp=emp.values_list('ID', 'Name', 'Dept', 'Salary', 'Job_code_id')
        try:
            emp=list(emp)[0]
        except:
            pass
        print(emp)
        job=Job.objects.values_list().filter(Code=emp[4])
        job=list(job)[0]
        if(att<24):
            job=list(job)
            job[2]=int(job[2]/2)
            job[3]=job[3]//2
            job=tuple(job)
        success=False
        return render(request, 'issue_salary.html', {'flag':flag, 'dep_list':dep_list,'emp':emp, 'job':job, 'att':att, 'success:':success})
    elif request.method=="POST":
        form=list(dict(request.POST).values())
        val=[]
        for i in range(1, len(form)):
            a=form[i][0]
            val.append(a)
        sno=Transactions.objects.values_list('Sno')
        sno=sno.aggregate(sno=Max('Sno'))
        sno=sno['sno']
        if not sno:
            sno=0
        sno+=1
        val.insert(0, sno)
        date=datetime.today().strftime('%Y-%m-%d')
        val.insert(4,date)
        
        form=Transactions(Sno=val[0], ID=Employee.objects.get(ID=val[1]), DID=Department.objects.get(Dep_ID=val[2]), Attendance=val[3], PDate=val[4], Salary=val[5], HRA=val[6], TA=val[7], DA=val[8], PF=val[9], IT=val[10])
        form.save()
        #Process PF Report
        bank=Bank_Details.objects.filter(ID=Employee.objects.get(ID=val[1])).values_list()
        try:
            bank=bank[0]
        except:
            pass

        sno=PFReport.objects.values_list('Sno')

        sno=sno.aggregate(sno=Max('Sno'))
        sno=sno['sno']
        if not sno:
            sno=0
        sno+=1
        pf=PFReport(Sno=sno, Accno=bank[2], IFSC=bank[3], Bank_Name=bank[4], PFAmount=val[9], Date=val[4])
        pf.save()
        success=True
        return render(request, 'issue_salary.html', {'flag':0, 'dep_list':dep_list, 'success:':success})
    else:
        pass


def monthly_report(request):
    if request.method=="POST":
        mon=request.POST['mon']
        mname=calendar.month_name[int(mon[5:])]
        print(mon)
        tot=Transactions.objects.filter(PDate__year=int(mon[:4]))
        tot=tot.filter(PDate__month=int(mon[5:])).values_list()
        agg=[]
        a=tot.aggregate(su=Sum('Salary'))
        a=a['su']
        agg.append(a)
        a=tot.aggregate(su=Sum('HRA'))
        a=a['su']
        agg.append(a)
        a=tot.aggregate(su=Sum('TA'))
        a=a['su']
        agg.append(a)
        a=tot.aggregate(su=Sum('DA'))
        a=a['su']
        agg.append(a)
        a=tot.aggregate(su=Sum('PF'))
        a=a['su']
        agg.append(a)
        a=tot.aggregate(su=Sum('IT'))
        a=a['su']
        agg.append(a)
        flag=False
        return render(request, 'monthly_report.html', {'flag':flag, 'month':mname, 'year':mon[:4], 'tot':tot, 'agg':agg})
    else:
        flag=True
        return render(request, 'monthly_report.html', {'flag':flag,})

def annual_report(request):
    if request.method=="POST":
        year=request.POST['year']
        
        tot=Transactions.objects.filter(PDate__year=int(year)).values_list()
        
        
        agg=[]
        a=tot.aggregate(su=Sum('Salary'))
        a=a['su']
        agg.append(a)
        a=tot.aggregate(su=Sum('HRA'))
        a=a['su']
        agg.append(a)
        a=tot.aggregate(su=Sum('TA'))
        a=a['su']
        agg.append(a)
        a=tot.aggregate(su=Sum('DA'))
        a=a['su']
        agg.append(a)
        a=tot.aggregate(su=Sum('PF'))
        a=a['su']
        agg.append(a)
        a=tot.aggregate(su=Sum('IT'))
        a=a['su']
        agg.append(a)
        tot=list(tot)
        flag=False
        return render(request, 'annual_report.html', {'flag':flag, 'year':year, 'tot':tot, 'agg':agg})
    else:
        flag=True
        return render(request, 'annual_report.html', {'flag':flag,})
    
def modify_emp(request):
    if request.method=="GET":
        flag=False
        try:
            service=request.GET['service']
        except:
            flag=True
            form=bank
            return render(request, 'modify_emp.html', {'flag':flag,})
        if(service=='Edit Bank Details'):
            form=bank
            return render(request, 'modify_emp.html', {'flag':flag, 'det':True, 'form':form})
        else:
            form=EmployeeForm
            return render(request, 'modify_emp.html', {'flag':flag, 'det':False, 'form':form})
    else:
        flag=True
        id=request.POST['EID']
        Bname=request.POST['BName']
        ifsc=request.POST['IFSC']
        acc=request.POST['accno']
        form=Bank_Details(ID=Employee.objects.get(ID=int(id)), Accno=acc, IFSC=ifsc, Bank_Name=Bname)
        form.save()
        return render(request, 'modify_emp.html', {'flag':flag, })
    
def PF_Report(request):
    if(request.method=="POST"):
        flag=False
        date_from=request.POST['from']
        date_to=request.POST['to']
        data=list(PFReport.objects.filter(Date__range=[date_from, date_to]).values_list())
        print(data)
        return render(request, 'PFReport.html', {'flag':flag, 'data':data,})
    else:
        flag=True
        return render(request, 'PFReport.html', {'flag':flag})
    
def emp_sal_list(request):
    emp=Employee.objects.values_list('ID', 'Name', 'Job_code_id', 'Salary')
    emp=list(emp)
    job=Job.objects.values_list('HRA', 'TA', 'DA', 'PF', 'IT')
    job=list(job)
    data=[]
    for i in emp:
        details=list(i)
        total=details[3]
        details[3]=details[3]//2
        id=int(details[2])
        jo=list(job[id-1])
        details.pop(2)
        details=details+jo
        net=sum(details[2:])
        details.append(max(0,total-(net+details[-2])))
        details.append(int((net+details[-1])*0.82))
        data.append(details)
    print(data)
    data=tuple(data)
   
    return render(request, 'emp_sal_list.html', {'data':data,})