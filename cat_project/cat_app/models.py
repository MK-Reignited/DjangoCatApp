from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, unique=True)
    number_of_cats = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name
class Pet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name