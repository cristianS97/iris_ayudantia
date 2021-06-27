from django.forms.forms import Form
from django.shortcuts import render
from .forms import IrisForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

# Create your views here.
class IndexFormView(FormView):
    template_name = 'index/index.html'
    form_class = IrisForm
    success_url = 'result/'
    
    def form_valid(self, form):
        sepal_length = form.cleaned_data['sepal_length']
        sepal_width = form.cleaned_data['sepal_width']
        petal_length = form.cleaned_data['petal_length']
        petal_width = form.cleaned_data['petal_width']
        print(sepal_length, sepal_width, petal_length, petal_width)
        return super().form_valid(form)

class ResultTemplateView(TemplateView):
    template_name = 'index/resultado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.GET)
        return context
    