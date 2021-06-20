from django.contrib import admin
from django.db import models

# Create your models here.
class Pipeline(models.Model):
    directorate = models.CharField('Directorate', max_length=10, choices=[('Pub-1', 'Pub-1'), ('Pub-2', 'Pub-2'), ('Pub-3', 'Pub-3'), ('Pri-1', 'Pri-1'), ('Pri-2', 'Pri-2')])
    ambm = models.CharField('AM/BM Name', max_length=30)
    pid = models.CharField('Prospect ID', max_length=10, unique=True)
    client = models.CharField('Client Name', max_length=50)
    project = models.CharField('Project Name', max_length=50)
    onetime = models.BooleanField('One-time', default=True)
    nmonth = models.IntegerField('x Months', default=1)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    order_dd = models.DateField('SO Date')
    order_val = models.DecimalField('Value', max_digits=14, decimal_places=0)
    gpm = models.DecimalField('GPM (%)', max_digits=6, decimal_places=2)
    bast_dd = models.DateField('BAST Date')


    def __str__(self):
        return self.pid

    # Reformat order_dd
    def format_order_dd(self):
        return self.order_dd.strftime('%b-%y')

    # Reformat bast_dd
    @admin.display(description='BAST Date')
    def format_bast_dd(self):
        return self.bast_dd.strftime('%b-%y')

    # Column Header
    format_order_dd.short_description = 'SO Date'

    # Reformat order_val to in Million with thousand separator
    @admin.display(description='Value') # Column Header
    def format_order_val(self):
        order_mil = self.order_val / 1000000
        formatted_number = str(format(order_mil, ',.0f'))
        padding = 9 - len(formatted_number)
        new_format = '_' * padding + formatted_number
        return new_format


    def order_val_inmill(self):
        inmill = self.order_val / 1000000
        return format(inmill, ',.0f')

    # Reformat gpm to align right and add %
    @admin.display(description='G P M') # Column Header
    def format_gpm(self):
        formatted_gpm = format(self.gpm, '.2f')
        return f"{formatted_gpm}%"

    class Meta:
        verbose_name_plural = "Sales Pipelines"
        ordering = ['directorate', 'order_dd', 'level', '-order_val']


class Level(models.Model):
    level = models.CharField('Level', max_length=2)
    weight = models.DecimalField('Weight', max_digits=6, decimal_places=2) #in %
    ordering = models.IntegerField('Ordering', null=True)

    def __str__(self):
        return self.level
    
    @admin.display(description='Weight %') # Column Header
    def format_weight(self):
        from django.utils.html import format_html
        formatted_weight = format(self.weight, ',.2f')
        return f"{formatted_weight}%"

    class Meta:
        verbose_name_plural = "Levels"
        ordering = ['ordering']