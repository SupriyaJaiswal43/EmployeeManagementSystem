from django.shortcuts import render,redirect
import mysql.connector as sql
from django.http import HttpResponseRedirect
from django.contrib import messages
id=''
pwd=''

    
# Create your views here.
def Admin_Login(request):
    global id,pwd
    if request.method=="POST":
        m=sql.connect(host='localhost',user='root',passwd='Supriya@123',database='emp_admin_login')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="AdminID":
                id=value
            if key=="password":
                pwd=value
            
        c="select * from admin_login where AdminID='{}' and Admin_Password='{}'".format(id,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.info(request, 'Either Admin Id or Password is invalid !')
        else:  # This uses the name of the URL pattern
            return HttpResponseRedirect('/employees/')

    return render(request,'Admin_Login.html')
# Create your views here.


def logout_ad(request):
    request.session.clear()
    return redirect('Admin Login/')