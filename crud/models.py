from django.db import models

# Create your models here.
class Pipeline(models.Model):
    directorate = models.CharField(max_length=10, choices=[('Public-1', 'Public-1'), ('Public-2', 'Public-2'), ('Public-3', 'Public-3'), ('Private-1', 'Private-1'), ('Private-2', 'Private-2')])
    ambm = models.CharField(max_length=30)
    pid = models.CharField(max_length=10, unique=True)
    client = models.CharField(max_length=50)
    project = models.CharField(max_length=50)
    rental = models.BooleanField(default=False)
    nmonth = models.IntegerField
    level = models.CharField(max_length=2)
    order_dd = models.DateField
    order_val = models.DecimalField(max_digits=17, decimal_places=2)
    gpm = models.DecimalField(max_digits=6, decimal_places=2)
    bast_dd = models.DateField
