from django.db import models

# Create your models here.
class Accounts(models.Model):
    userName=models.CharField(max_length=122)
