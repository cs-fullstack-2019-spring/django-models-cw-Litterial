from django.db import models

# Create your models here.




class Dog(models.Model):
    name=models.CharField(max_length=50)       #name
    breed=models.CharField(max_length=50)      #breed
    color=models.CharField(max_length=50)      #colors
    gender=models.CharField(max_length=50)     #gender

class newAccount(models.Model):
    userName=models.CharField(max_length=50)   #username
    realName=models.CharField(max_length=80)   #realname
    accountNumber=models.IntegerField(default=0)   #account number
    accountBalance=models.DecimalField(decimal_places=2,max_digits=12)   #account balance

