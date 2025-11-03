from django.db import models


#---------------- LAB 8 -------------------
class Address(models.Model):
    city=models.CharField(max_length=255)


class Student(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    