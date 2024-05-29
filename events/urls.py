from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('new_dep/', views.new_dep, name="new_dep"),
    path('new_emp/', views.new_emp, name="new_emp"),
    path('view_dep/', views.view_dep, name="view_dep"),
    path('view_emp/', views.view_emp, name="view_emp"),
    path('issue_salary/', views.issue_salary, name="issue_salary"),
    path('monthly_report/', views.monthly_report, name="monthly_report"),
    path('annual_report/', views.annual_report, name="annual_report"),
    path('modify_emp/', views.modify_emp, name="modify_emp"),
    path('PFReport/', views.PF_Report, name="PFReport"),
    path('emp_sal_list/', views.emp_sal_list, name="emp_sal_list")
]