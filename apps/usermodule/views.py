from django.shortcuts import render

# Create your views here.

#---------------- LAB 8 -------------------
from .models import Address,Student
from django.db.models import Count
def lap8_task7(request):
    students_city_count = Student.objects.values('address__city').annotate(student_count=Count('id'))
    return render(request,'usermodule/lap8_task7.html', context={"students_city_count": students_city_count})
