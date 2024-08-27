from django.db import models

class Class(models.Model) :
    name = models.CharField(max_length=50 , null= False)
    time = models.TimeField(null= False)
    price = models.IntegerField(null= True)
    teacher = models.ManyToManyField('teacher_app.Teacher' , null= False , related_name= "teacher_name")
    category = models.ForeignKey('category_app.Category' , null= False , on_delete=models.CASCADE , related_name= "category_name")
    student = models.ManyToManyField('student_app.Student' , null= False , related_name= "student")
# Create your models here.
