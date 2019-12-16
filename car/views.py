from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, DetailView, ListView, CreateView, UpdateView
from .forms import CarForm, PenyewaanForm
from .models import Car, Penyewaan
from django.urls import reverse_lazy


def index(request):
    context = {
        'page': 'Car | Home',
        'judul': 'RentCar',
    }
    return render(request, 'car/index.html', context)


class SewaCreateView(LoginRequiredMixin, CreateView):
    form_class = PenyewaanForm
    template_name = 'car/create.html'
    extra_context = {
        'page': 'Car | Sewa'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        car = Car.objects.only('id').get(id=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.car = car
        return super().form_valid(form)


class CarListView(ListView):
    model = Car
    paginate_by = 2
    ordering = ['update']

    def get_queryset(self):
        if self.kwargs['pk'] != 'all':
            self.queryset = self.model.objects.filter(
                user=int(self.kwargs['pk']))
            self.kwargs.update({
                'pk': self.kwargs['pk']
            })
        return super().get_queryset()


class SewaListView(ListView):
    model = Penyewaan
    paginate_by = 20
    ordering = ['tgl_sewa']

    def get_queryset(self):
        self.queryset = self.model.objects.filter(
            user=self.request.user)
        return super().get_queryset()


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = reverse_lazy("car:list", args={1})


class CarUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CarForm
    model = Car
    template_name = 'car/create.html'
    extra_context = {
        'page': 'Car | Update'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)


class CarCreateView(LoginRequiredMixin, CreateView):
    form_class = CarForm
    template_name = 'car/create.html'
    extra_context = {
        'page': 'Car | Create'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CarDetailView(DetailView):
    model = Car
    extra_context = {
        'page': 'Car | Detail'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)
