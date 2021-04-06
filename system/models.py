from django.db import models

# Create your models here.
class Customer(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    balance=models.CharField(max_length=100)

class Transaction_history(models.Model):
    sender=models.ForeignKey(Customer,on_delete=models.CASCADE)
    reciever=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)