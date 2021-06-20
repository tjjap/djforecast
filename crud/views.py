from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from crud.models import Pipeline

# Create your views here.
def index(request):
    return render(request, "crud/index.html")

class PipelineListView(ListView):
    model = Pipeline
    template_name = "pipeline_list.html"
    paginate_by = 5
