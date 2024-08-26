from django.db import models

class Factor(models.Model) :
    student_name = models.CharField(max_length=50)
    price = models.FloatField()
    cupon = models.ForeignKey("cupon_app.Cupon", on_delete=models.CASCADE)
    class1 = models.ForeignKey("class_app.Class", on_delete=models.CASCADE)
    payment_status = models.BooleanField()


# Create your models here.
