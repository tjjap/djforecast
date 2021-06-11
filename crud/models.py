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
    level = models.CharField('Level', max_length=2, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D+', 'D+'), ('D', 'D'), ('E', 'E')])
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
        from django.utils.html import format_html
        order_mil = self.order_val / 1000000
        formatted_number = format(order_mil, ',.0f')
        return format_html("<p style='text-align:right;'>{}</p>", formatted_number)

    # Reformat gpm to align right and add %
    @admin.display(description='== GPM ==') # Column Header
    def format_gpm(self):
        from django.utils.html import format_html
        formatted_gpm = format(self.gpm, ',.2f')
        return format_html("<p style='text-align:right;'>{}%</p>", formatted_gpm)

    class Meta:
        verbose_name_plural = "Sales Pipelines"
        ordering = ['order_dd', 'level', '-order_val']