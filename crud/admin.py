from django.contrib import admin
from .models import Pipeline
from django.conf.locale.es import formats as es_formats


# Customize Admin Panel (Edit Panel) 
class PipelineAdmin(admin.ModelAdmin):
    list_filter = ("directorate", "ambm")
    list_display = ("directorate", "ambm", "pid", "client", "project", "level", "format_order_val", "format_gpm", "format_order_dd", "rental")

# Register your models here.
admin.site.register(Pipeline, PipelineAdmin)


