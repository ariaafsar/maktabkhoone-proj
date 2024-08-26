from django.db import models

class Class(models.Model) :
    name = models.CharField(max_length=50)
    time = models.TimeField()
    price = models.IntegerField()
    teacher = models.ForeignKey('teacher_app.Teacher' , on_delete=models.CASCADE , related_name= "teacher_name")
    category = models.ForeignKey('category_app.Category' , on_delete=models.CASCADE , related_name= "category_name")
    student = models.ManyToManyField("student_app.Student")
# Create your models here.
