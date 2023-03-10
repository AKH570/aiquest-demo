from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.FloatField()
    discount= models.FloatField()
    description = models.TextField()
    prod_img = models.ImageField(upload_to='prodimg')
    


    def __str__(self):
        return self.product_name
    