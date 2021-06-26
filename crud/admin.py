from crud.forms import PipelineForm
from django.contrib import admin
from django import forms
from django.contrib.admin.options import ModelAdmin
from .models import Pipeline, Level
from django.conf.locale.es import formats as es_formats
from django.db import models
from django.forms.widgets import TextInput, Textarea


# Customize Admin Panel (Edit Panel)

class PipelineAdmin(admin.ModelAdmin):
    list_filter = ("directorate", "ambm")
    list_display = ("directorate", "ambm", "pid", "client", "project", "onetime", "nmonth", "level", "format_order_val", "format_gpm", "format_order_dd", "format_bast_dd",)
    #list_display = ("format_order_val", "directorate", "ambm", "pid", "client", "project", "level", "format_order_val")
    date_hierarchy = 'order_dd'
    form = PipelineForm #to be able to use custom validation defined in the form
    


class LevelAdmin(admin.ModelAdmin):
    list_display = ("level", "format_weight",)


# Register your models here.
admin.site.register(Pipeline, PipelineAdmin)
admin.site.register(Level, LevelAdmin)


