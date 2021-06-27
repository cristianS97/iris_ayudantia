from django.urls import path
from .views import IndexFormView, ResultTemplateView

urlpatterns = [
    path('', IndexFormView.as_view(), name='index'),
    path('result/', ResultTemplateView.as_view(), name='result')
]
