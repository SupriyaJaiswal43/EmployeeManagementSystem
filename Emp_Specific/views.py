from django.shortcuts import render, get_object_or_404
from Landing_EMP.models import Employee  
import mysql.connector as sql

def employee_listfor1(request,EmployeeID):
    employees = Employee.objects.filter(employeeid=EmployeeID).values()
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
