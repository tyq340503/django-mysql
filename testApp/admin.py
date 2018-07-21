from django.contrib import admin

# Register your models here.
from .models import TestGrade,TestStudent

class AddStu(admin.TabularInline):
    model= TestStudent
    extra=2

@admin.register(TestGrade)
class Admin(admin.ModelAdmin):
    inlines=[AddStu]
    list_display = ['pk','name','date','girlnum','boynum','isdelete']
    list_filter=[]
    list_per_page=10
    search_fields=[]
    fields = ['name','date','girlnum','boynum','isdelete']

    # def __str__(self):
    #     return self.name

@admin.register(TestStudent)
class StudentAdmin(admin.ModelAdmin):
    def showgender(self):
        if self.gender:
            return 'male'
        else:
            return 'female'
    showgender.short_description = 'gender'
    list_display = ['pk','name','scont',showgender,'age','isdelete','tgrade']
    list_filter=[]
    list_per_page=10
    search_fields=[]
    fields = ['name','scont','gender','age','isdelete','tgrade']
    

    # def __str__(self):
    #     return self.name

# admin.site.register(TestGrade,Admin)
# admin.site.register(TestStudent,StudentAdmin)