from django.db import models

# Create your models here.
class property_detail(models.Model):
    title=models.CharField(max_length=50)
    tage=models.CharField(max_length=10)
    location=models.TextField()
    area=models.IntegerField()
    property_type=models.CharField(max_length=15)
    bed=models.IntegerField()
    carparking=models.IntegerField()
    


