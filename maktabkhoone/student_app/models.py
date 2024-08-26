from django.db import models

class Student(models.Model) :
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    class1 = models.ManyToManyField("class_app.Class")
    cupon = models.OneToOneField("cupon_app.Cupon", on_delete=models.CASCADE)
    wallet = models.IntegerField(default= 0)
# Create your models here.
                                                              