from django.shortcuts import render,redirect
import mysql.connector as sql
from django.http import HttpResponseRedirect
from django.contrib import messages


id=''
pwd=''

# Create your views here.
def Employee_Action(request):
    global id,pwd
    if request.method=="POST":
        m=sql.connect(host='localhost',user='root',passwd='Supriya@123',database='emp_admin_login')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="EmployeeID":
                id=value
            if key=="password":
                pwd=value
            
        c="select * from employee_login where EmployeeID='{}' and Password='{}'".format(id,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.info(request, 'Either Employee Id or Password is invalid !')
        else:
            return HttpResponseRedirect('/empfor1/{}/'.format(id))
        
    return render(request,'Employee_Login.html')



