
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Student
from .forms import Studentform
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


# READ: Show one student
class students_details(DetailView):
    model = Student
    template_name = 'students_details.html'
    context_object_name = 'student' #for the object in html
    pk_url_kwarg = 'id'  #for int in urls.py 

# CREATE: Add a student
class add_students(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Student
    form_class = Studentform                      #as add student contains form.py
    template_name = 'add_students.html'
    success_url = reverse_lazy('home')            # Redirect to the 'name=home' after successful submission
    permission_required = 'students.add_student'


# UPDATE: Edit a student
class edit_student(UpdateView):
    model = Student
    form_class = Studentform
    template_name = 'edit_student.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


# DELETE: Delete a student
class delete_student(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
