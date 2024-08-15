from django.db import models


class Bank(models.Model):
    acc_no = models.CharField(max_length=50) # Example field
    acc_holder = models.CharField(max_length=50)
    acc_balance = models.DecimalField(max_digits=10, decimal_places=2)  # Example field