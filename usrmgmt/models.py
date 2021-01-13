from django.db import models

# Create your models here.

class Users(models.Model):
    U_ID = models.AutoField(primary_key=True, serialize=False)
    NAME = models.CharField(max_length=100, blank=False, default='')
    EMAIL = models.EmailField(blank=False, default='')
    PHONE = models.IntegerField(blank=False, default='')
    ADDR = models.CharField(max_length=500, blank=False, default='')
    TIMESTAMP = models.DateTimeField(auto_now_add=True)