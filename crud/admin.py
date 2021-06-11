from django.contrib import admin
from django import forms
from .models import Pipeline
from django.conf.locale.es import formats as es_formats
from django.db import models
from django.forms.widgets import TextInput, Textarea


# Customize Admin Panel (Edit Panel)

class PipelineAdmin(admin.ModelAdmin):
    list_filter = ("directorate", "ambm")
    list_display = ("directorate", "ambm", "pid", "client", "project", "level", "format_order_val", "format_gpm", "format_order_dd", "rental")
    #list_display = ("format_order_val", "directorate", "ambm", "pid", "client", "project", "level", "format_order_val")
    date_hierarchy = 'order_dd'
    

    # formfield_overrides = {
    #     models.DecimalField: {
    #         'widget': forms.Textarea(attrs={'style': 'text-align:right;',}),
    #     }
    # }


# Register your models here.
admin.site.register(Pipeline, PipelineAdmin)


