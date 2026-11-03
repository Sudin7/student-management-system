from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from students.models import Student

class home(ListView):  #LoginREquiredMixin helps only login in user to go to home
    model = Student
    template_name = 'home.html'
    context_object_name = 'students'  # This matches the 'students' key in your template
