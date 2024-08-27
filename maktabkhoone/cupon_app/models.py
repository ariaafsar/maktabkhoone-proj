from django.db import models

class Cupon(models.Model) :
    name = models.CharField(max_length=50 , null= False)
    percent = models.IntegerField(null= False)
    expire_date = models.DateField(auto_now=False, null= True , auto_now_add=False)
# Create your models here.
