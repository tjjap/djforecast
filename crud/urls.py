from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('list/', views.PipelineListView.as_view(), name='pipeline-list'),
]