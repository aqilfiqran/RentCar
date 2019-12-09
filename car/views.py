from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .forms import CarForm
from .models import Car


def index(request):
    context = {
        'page': 'homeCar'
    }

    return render(request, 'car/index.html', context)


class CarCreateView(CreateView):
    form_class = CarForm
    template_name = 'car/create.html'

    extra_context = {
        'page': 'Car | Create'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)


class CarDetailView(DetailView):
    model = Car
    extra_context = {
        'page': 'Car | Detail'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)
