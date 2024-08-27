from django.db import models

class Teacher(models.Model) :
    name = models.CharField(max_length=50 , null= False)
    email = models.EmailField(max_length=254 , null= False)
    phone_number = models.CharField(max_length=15 , default="000000000000000" , null= False)
    rate = models.FloatField(null= True)
    category = models.ManyToManyField('category_app.Category' , null= True , related_name= "category")
    clas = models.ManyToManyField('class_app.Class' , verbose_name="class" , null= True , related_name= "clas")
    wallet = models.IntegerField(default= 0)
    
# Create your models here.  