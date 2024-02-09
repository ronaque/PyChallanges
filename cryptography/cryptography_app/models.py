from django.db import models

# Create your models here.
class Cryptography(models.Model):
    userDocument = models.CharField(max_length=128)
    creditCardToken = models.CharField(max_length=128)
    value = models.IntegerField()