from django.db import models

# Create your models here.
# from testApp.models import TestGrade,TestStudents
# from django.utils import timezone
# from datetime import *

class TestGrade(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    girlnum = models.IntegerField()
    boynum = models.IntegerField()
    isdelete = models.BooleanField()

class StuManager(models.Manager):
    def filterDel(self):
        return super(StuManager,self).filterDel().filter(isdelete=False)
    
    def createStu(self,name,gender,age,scont,tgrade,lastTime,createTime,isdelete = False):
        stu = self.model()
        stu.name = name
        stu.gender = gender
        stu.age = age
        stu.scont = scont        
        return stu

class TestStudent(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default = True)
    age = models.IntegerField()
    scont = models.CharField(max_length=20)
    isdelete = models.BooleanField(blank=True)
    tgrade = models.ForeignKey("TestGrade")
    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'student'
        ordering = ['id']

    @classmethod
    def addStu(cls,name,gender,age,scont,tgrade,lastTime,createTime,isdelete = False):
        stu = cls(name=name,gender=gender,age=age,scont=scont,isdelete=isdelete,tgrade=tgrade,lastTime=lastTime,createTime=createTime)
        return stu

