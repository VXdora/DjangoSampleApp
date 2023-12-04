from django import http
from django.shortcuts import render
from .models import Item, Category

# Create your views here.
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'shopping/index.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        context['categories'] = Category.objects.all()
        return context

from django.views.generic import DetailView
class DetailView(DetailView):
    template_name = 'shopping/detail.html'
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context