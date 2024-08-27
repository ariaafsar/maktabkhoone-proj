from django.db import models

class Class(models.Model) :
    name = models.CharField(max_length=50 , null= False)
    time = models.TimeField(null= False)
    price = models.IntegerField(null= True)
    teacher = models.ManyToManyField('teacher_app.Teacher' , blank= True , related_name= "teacher_name")
    category = models.ForeignKey('category_app.Category' , blank= True , on_delete=models.CASCADE , related_name= "category_name")
    student = models.ManyToManyField('student_app.Student' , blank= True , related_name= "student")
# Create your models here.
