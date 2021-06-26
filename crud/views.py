from .forms import PipelineForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from crud.models import Pipeline
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "crud/index.html")

class PipelineListView(ListView):
    model = Pipeline
    template_name = "crud/pipeline_list.html"
    paginate_by = 5

class PipelineDetailView(DetailView):
    model = Pipeline
    #template_name = "crud/pipeline_detail.html" --> if using standard pattern no need to specify

class AddPipelineCreateView(SuccessMessageMixin, CreateView):
    model = Pipeline
    #fields = '__all__'  not needed because already stated in PipelineForm(ModelForm)
    form_class = PipelineForm
    template_name = "crud/add.html"
    success_url = reverse_lazy('pipeline-create')
    success_message = "%(pid)s : %(client)s --- was created successfully"


class PipelineUpdateView(SuccessMessageMixin, UpdateView):
    model = Pipeline
    #fields = '__all__'  not needed because already stated in PipelineForm(ModelForm)
    form_class = PipelineForm
    template_name = "crud/pipeline_update.html"
    success_url = reverse_lazy('pipeline-list')
    success_message = "%(pid)s : %(client)s --- was updated successfully"


class PipelineDeleteView(DeleteView):
    model = Pipeline
    template_name = "crud/pipeline_delete.html"
    success_url = reverse_lazy('pipeline-list')
    success_message = "%(pid)s : %(client)s --- was deleted successfully"
    
    #SuccessMessageMixin is not used in the delete-view, must use delete function below
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(PipelineDeleteView, self).delete(request, *args, **kwargs)

