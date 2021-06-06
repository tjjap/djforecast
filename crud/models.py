from django.db import models

# Create your models here.
class Pipeline(models.Model):
    directorate = models.CharField('Directorate', max_length=10, choices=[('Public-1', 'Public-1'), ('Public-2', 'Public-2'), ('Public-3', 'Public-3'), ('Private-1', 'Private-1'), ('Private-2', 'Private-2')])
    ambm = models.CharField('AM/BM Name', max_length=30)
    pid = models.CharField('Prospect ID', max_length=10, unique=True)
    client = models.CharField('Client Name', max_length=50)
    project = models.CharField('Project Name', max_length=50)
    rental = models.BooleanField('Rental/Mngd Service', default=False)
    nmonth = models.IntegerField('x Months')
    level = models.CharField('Level', max_length=2)
    order_dd = models.DateField('SO Booking DD')
    order_val = models.DecimalField('Value', max_digits=14, decimal_places=0)
    gpm = models.DecimalField('GPM (%)', max_digits=6, decimal_places=2)
    bast_dd = models.DateField('BAST Date')
