from django.db import models

class Student(models.Model) :
    name = models.CharField(max_length=50 , null= False)
    email = models.EmailField(max_length=254 , null= False)
    phone_number = models.CharField(max_length=15 , default= "000000000000000" , null= False)
    clas = models.ManyToManyField('class_app.Class' , verbose_name="class" , blank= True , related_name= "clss")
    cupon = models.ForeignKey('cupon_app.Cupon', null= True , on_delete=models.CASCADE , related_name= 'cupn')
    wallet = models.IntegerField(default= 0)
# Create your models here.
                                                              