from django.shortcuts import render,redirect
import io
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth import logout

def index(request):
    return HttpResponse('this is testapp index')

from .models import TestGrade, TestStudent

def grades(request):
    gradesList = TestGrade.objects.all()
    return render(request, 'testApp/grade.html', {"grades":gradesList})

def gradedetail(request,id):
    grade = TestGrade.objects.get(pk=id)
    stuList = grade.teststudent_set.all() 
    return render(request, 'testApp/grade.html', {"grades":stuList})

def stu(request):
    stuList = TestStudent.objects.all()
    return render(request, 'testApp/stu.html', {"students":stuList})

def add(request):
    grade = TestGrade.objects.get(pk=1)
    stuadd = TestStudent.addStu("name",1,12,"scont",grade,"2018-9-1","2018-9-1")
    stuadd.save()
    return render(request, 'testApp/add.html', {"students":stuadd})

def redir(request):
    # stuList = TestStudent.objects.all()
    return HttpResponseRedirect('testApp/stu.html')

def verifyImg(request):
    buf = io.BytesIO()
    # im.save(buf,'png')
    return HttpResponse(buf.getvalue(),'img/png')