from django.db import models

# Create your models here.
class degree(models.Model):
    degree_name=models.CharField(max_length=100)
    university=models.CharField(max_length=100)


    def __str__(self):
        return f"{self.degree_name} {self.university}"

class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='student_images/',default='default.jpg')
    age=models.IntegerField()
    semester=models.CharField(max_length=10)
    degree_name=models.ForeignKey(degree, on_delete=models.SET_NULL, null=True)
    is_graduated=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age} {self.semester} {self.degree_name} {self.is_graduated}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
