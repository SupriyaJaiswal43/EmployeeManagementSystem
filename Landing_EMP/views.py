from django.shortcuts import render
from Landing_EMP.models import Employee  
from django.http import HttpResponse
import mysql.connector as sql


def employee_list(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    
    '''m=sql.connect(host='localhost',user='root',passwd='Krrish1234',database='emp_admin_login')
    cursor=m.cursor()
    c="select * from employee"
    cursor.execute(c)
    employee=tuple(cursor.fetchall())
    for i in employee:
        print(i)'''
    return render(request, 'Landing_EMP.html', context )
