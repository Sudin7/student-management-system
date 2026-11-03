from django.urls import path
from . import views

urlpatterns = [
    path('degrees/', views.DegreeView.as_view()),
    path('degrees/<int:pk>/', views.DegreeView.as_view()),
    path('students/', views.StudentView.as_view()),
    path('students/<int:pk>/', views.StudentView.as_view()),
]
