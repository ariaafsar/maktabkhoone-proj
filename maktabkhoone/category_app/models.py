from django.db import models

class Category(models.Model) :
    name = models.CharField(verbose_name= "name" , max_length=50)
    class1 = models.ForeignKey("class_app.Class", on_delete=models.CASCADE)
# Create your models here.
