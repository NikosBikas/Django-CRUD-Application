from django.db import models

# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Course(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Trainer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
