from django.db import models


# Create your models here.


class District(models.Model):
    name=models.CharField(max_length=800)
    def __str__(self):
        return '{}'.format(self.name)

class City(models.Model):
    name=models.CharField(max_length=800)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

class Register(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    district=models.ForeignKey(District,on_delete=models.SET_NULL, null=True,blank=True)
    city=models.ForeignKey(City,on_delete=models.SET_NULL, null=True,blank=True)
    account= models.CharField(max_length=200)
    material = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)
