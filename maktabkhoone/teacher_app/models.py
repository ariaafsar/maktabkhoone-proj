from django.db import models

class Teacher(models.Model) :
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    rate = models.FloatField()
    category = models.ForeignKey("category_app.Category", on_delete=models.CASCADE)
    class1 = models.ManyToManyField("class_app.Class")
    wallet = models.IntegerField(default= 0)
    
# Create your models here.  