from django.db import models

# Create your models here.
class property_detail(models.Model):
    title = models.CharField(max_length=255)
    location = models.TextField()
    contact = models.CharField(max_length=10)
    alternative_contact = models.CharField(max_length=10, blank=True, null=True)
    facilities = models.TextField()
    property_details = models.TextField()
    property_area = models.DecimalField(max_digits=10, decimal_places=2)
    price =models.IntegerField()
    property_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    
    # Additional fields for House properties
    furnishing = models.CharField(max_length=50, blank=True)
    bedroom = models.IntegerField()
    kitchen = models.IntegerField()
    living_room = models.IntegerField()
    bathroom = models.IntegerField()
    car_parking = models.IntegerField()
    


