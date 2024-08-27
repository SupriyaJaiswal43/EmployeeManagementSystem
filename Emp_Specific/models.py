from django.db import models

class Employee(models.Model):
    employeeid = models.IntegerField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_Name', max_length=100)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=15)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=10, decimal_places=2)  # Field name made lowercase.
    date_of_joining = models.DateField(db_column='Date_of_Joining')  # Field name made lowercase.
    document = models.CharField(db_column='Document', max_length=200, blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager()

    def __str__(self):
        return self.Full_Name

    class Meta:
        managed = False
        db_table = 'employee'
    
