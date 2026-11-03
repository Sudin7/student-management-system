
from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:id>/',views.students_details.as_view(),name='students_details'),
    path(
        'add/',
        views.add_students.as_view(),
        name='add_students'
    ),
    path(
        'edit/<int:id>/',
        views.edit_student.as_view(),
        name='edit_student'
    ),
    path(
        'delete/<int:id>/',
        views.delete_student.as_view(),
        name='delete_student'
    ),
]
