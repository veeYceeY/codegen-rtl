from django.db import models

# Create your models here.
class employee(models.Model):
    emp_name=models.CharField(max_length=100,default='')
    image=models.ImageField(upload_to="empimages",max_length=100,default="")
    email=models.CharField(max_length=100,default='')
    password=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=100,default='')
    address=models.CharField(max_length=100,default='')
    dob=models.CharField(max_length=100,default='')
    doj=models.CharField(max_length=100,default='')
    designation=models.CharField(max_length=100,default='')
    salary=models.CharField(max_length=100,default='')
    usertype=models.CharField(max_length=100,default='')
    username=models.CharField(max_length=30,default='')



