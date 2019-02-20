from django.db import models

# Create your models here.


class Dog(models.Model):
    name=models.CharField(max_length=50)
    breed=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)

class newAccount(models.Model):
    userName=models.CharField(max_length=50)
    realName=models.CharField(max_length=80)
    accountNumber=models.IntegerField(default=0)
    accountBalance=models.DecimalField(decimal_places=2,max_digits=12)

