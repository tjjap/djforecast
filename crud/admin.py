from django.contrib import admin
from .models import Pipeline
from django.conf.locale.es import formats as es_formats


# Customize Admin Panel (Edit Panel) 
class PipelineAdmin(admin.ModelAdmin):
    list_filter = ("directorate", "ambm")
    list_display = ("directorate", "ambm", "pid", "client", "project", "level", "order_val", "format_date", "rental")

    def format_date(self, obj):
        return obj.order_dd.strftime('%b-%y')

    format_date.admin_order_field = 'order_dd'
    format_date.short_description = 'SO Date'

# Register your models here.
admin.site.register(Pipeline, PipelineAdmin)


