from django.contrib import admin
from django.db import models

# Create your models here.
class Pipeline(models.Model):
    directorate = models.CharField('Directorate', max_length=10, choices=[('Public-1', 'Public-1'), ('Public-2', 'Public-2'), ('Public-3', 'Public-3'), ('Private-1', 'Private-1'), ('Private-2', 'Private-2')])
    ambm = models.CharField('AM/BM Name', max_length=30)
    pid = models.CharField('Prospect ID', max_length=10, unique=True)
    client = models.CharField('Client Name', max_length=50)
    project = models.CharField('Project Name', max_length=50)
    rental = models.BooleanField('Rental', default=False)
    nmonth = models.IntegerField('x Months', default=1)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    order_dd = models.DateField('SO Booking DD')
    order_val = models.DecimalField('Value', max_digits=14, decimal_places=0)
    gpm = models.DecimalField('GPM (%)', max_digits=6, decimal_places=2)
    bast_dd = models.DateField('BAST Date')


    # Reformat order_dd
    def format_order_dd(self):
        return self.order_dd.strftime('%b-%y')

    # Column Header
    format_order_dd.short_description = 'SO Date'

    # Reformat order_val to in Million with thousand separator
    @admin.display(description='In Million Rp') # Column Header
    def format_order_val(self):
        order_mil = self.order_val / 1000000
        formatted_number = str(format(order_mil, ',.0f'))
        padding = 9 - len(formatted_number)
        new_format = '_' * padding + formatted_number
        return new_format


    # Reformat gpm to align right and add %
    @admin.display(description='== GPM ==') # Column Header
    def format_gpm(self):
        formatted_gpm = format(self.gpm, '.2f')
        return f"{formatted_gpm}%"

    class Meta:
        verbose_name_plural = "Sales Pipelines"
        ordering = ['order_dd', 'level', '-order_val']


class Level(models.Model):
    level = models.CharField('Level', max_length=2)
    weight = models.DecimalField('Weight', max_digits=6, decimal_places=2) #in %

    def __str__(self):
        return self.level
    
    @admin.display(description='Weight %') # Column Header
    def format_weight(self):
        from django.utils.html import format_html
        formatted_weight = format(self.weight, ',.2f')
        return f"{formatted_weight}%"

    class Meta:
        verbose_name_plural = "Levels"
        ordering = ['level']