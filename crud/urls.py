from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('list/', views.PipelineListView.as_view(), name='pipeline-list'),
    path('<int:pk>/', views.PipelineDetailView.as_view(), name='pipeline-detail'),
    path('create/', views.AddPipelineCreateView.as_view(), name='pipeline-create'),
    path('<int:pk>/update/', views.PipelineUpdateView.as_view(), name='pipeline-update'),
    path('<int:pk>/delete/', views.PipelineDeleteView.as_view(), name='pipeline-delete'),
]