from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    account_number = models.BigIntegerField(primary_key=True)
    balance = models.BigIntegerField();
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name;

    def get_absolute_url(self):
        return reverse("customer_list")

class Transaction(models.Model):
    sender_name = models.ForeignKey('Customer',related_name='sender', on_delete=models.CASCADE)
    receiver_name = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    date = models.DateTimeField(default= timezone.now)

    def __int__(self):
        return self.amount;
