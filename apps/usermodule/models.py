from django.db import models


#---------------- LAB 8 -------------------
class Address(models.Model):
    city=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}"

class Student(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    
    


class Student2(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    address=models.ManyToManyField(Address)
    img = models.ImageField(upload_to="av/",null=True)
    