from django.db import models

# Create your models here.
class Signup(models.Model):
    f_name = models.CharField(max_length=100)
    gender = models.CharField()
    contactno = models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    state = models.CharField()
    district = models.CharField()
    city = models.CharField()
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.f_name
    
class Pickup(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    date = models.DateField('mm-dd-yyyy')
    time_slot = models.CharField(max_length=50)
    items = models.TextField()


    def __str__(self):
        return f"Pickup for {self.name} on {self.date} at {self.time_slot}"
    
class contactus(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField()


    def __str__(self):
        return f"Message from {self.name} ({self.email})"