from django.shortcuts import render,redirect

# Create your views here.

#---------------- LAB 8 -------------------
from .models import Address,Student
from django.db.models import Count
def lap8_task7(request):
    students_city_count = Student.objects.values('address__city').annotate(student_count=Count('id'))
    return render(request,'usermodule/lap8_task7.html', context={"students_city_count": students_city_count})



from .forms import StudentForm as sf,StudentForm2 as sf2
from .models import Student2
def read(request):
    students=Student.objects.all()
    return render(request,"usermodule/listStudents.html",{"students":students})


def create(request):
    if request.method=="POST":
        forms=sf(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("student.read")
            
    forms=sf()
    return render(request,"usermodule/lap11.html",{"forms":forms})

def update(request,id):
    try:
        student=Student.objects.get(id=int(id))
    except Exception as e:
        print(e)
        return redirect("student.read")
    if request.method=="POST":
        forms=sf(request.POST,instance=student)
        if forms.is_valid():
            forms.save()
            return redirect("student.read")
    forms=sf(instance=student)
    return render(request,"usermodule/lap11.html",{"forms":forms})

def delete(request,id):
    try:
        student=Student.objects.get(id=id)
        student.delete()
        return redirect("student.read")
    except Exception as e:
        return redirect("student.read")
    
    
    
    
    
    
    
    
def read2(request):
    students=Student2.objects.all()
    student=Student2.objects.get(id=1)
    return render(request,"usermodule/listStudents2.html",{"students":students,"student":student})


def create2(request):
    if request.method=="POST":
        forms=sf2(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect("student2.read")
            
    forms=sf2()
    return render(request,"usermodule/lap11.html",{"forms":forms})

def update2(request,id):
    try:
        student=Student2.objects.get(id=int(id))
    except Exception as e:
        print(e)
        return redirect("student2.read")
    if request.method=="POST":
        forms=sf2(request.POST,request.FILES,instance=student)
        if forms.is_valid():
            forms.save()
            return redirect("student2.read")
    forms=sf2(instance=student)
    return render(request,"usermodule/lap11.html",{"forms":forms})

def delete2(request,id):
    try:
        student=Student2.objects.get(id=id)
        student.delete()
        return redirect("student2.read")
    except Exception as e:
        return redirect("student2.read")