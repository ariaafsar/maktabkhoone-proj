from django.db import models

class Cupon(models.Model) :
    name = models.CharField(max_length=50)
    percent = models.IntegerField()
    expire_date = models.DateField(auto_now=False, auto_now_add=False)

# Create your models here.
