from django.forms.forms import Form
from django.shortcuts import render
from .forms import IrisForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
import joblib
from pathlib import Path

ruta = Path(__file__).resolve().parent

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
        return super().form_valid(form)

class ResultTemplateView(TemplateView):
    template_name = 'index/resultado.html'

    def post(self, request, *args, **kwargs):
        
        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']

        data = [sepal_length, sepal_width, petal_length, petal_width]
        data = [data]

        cls = joblib.load(ruta.joinpath('clasificador.pkl'))
        prediccion = cls.predict(data)[0]
        opciones = ['setosa', 'versicolor', 'virginica']

        context = {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width,
            'prediccion': opciones[prediccion]
        }

        return render(request, self.template_name, context)
