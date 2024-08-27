from django.db import models

class Factor(models.Model) :
    student_name = models.CharField(max_length=50 , null= False)
    price = models.FloatField(null= True)
    cupon = models.OneToOneField('cupon_app.Cupon' , null= True , on_delete=models.CASCADE , related_name="cupon")
    class1 = models.ForeignKey('class_app.Class' , verbose_name= "class" , null= True , on_delete=models.CASCADE)
    payment_status = models.BooleanField(default= False)

# Create your models here.
