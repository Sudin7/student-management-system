from django.contrib import admin
from .models import Student, degree

class StudentAdmin(admin.ModelAdmin):
    list_display=['full_name','age','semester','degree_name','is_graduated']
    search_fields=['full_name','last_name']
    list_editable=['is_graduated']

class degreeAdmin(admin.ModelAdmin):
    list_display=['id','degree_name','university']
    

# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(degree,degreeAdmin)