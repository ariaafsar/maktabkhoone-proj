from django.db import models

class Category(models.Model) :
    name = models.CharField(verbose_name= "name", null= False , max_length=50)
    clas = models.ForeignKey("class_app.Class" , verbose_name= "class" , blank= True , on_delete=models.CASCADE , related_name= "cls")
# Create your models here.
