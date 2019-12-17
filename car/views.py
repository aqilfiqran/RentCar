from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, DeleteView, DetailView, ListView, CreateView, UpdateView
from .forms import CarForm, PenyewaanForm
from .models import Car, Penyewaan
from django.urls import reverse_lazy


class About(TemplateView):
    template_name = 'car/about.html'
    extra_context = {
        'page': 'Rentcar | About'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)


class Index(View):
    extra_context = {
        'page': 'Car | Home',
        'judul': 'RentCar',
        'penjelasan': 'Car Rental for All Your Traveling Needs'
    }

    def get(self, request):
        return render(request, 'car/index.html', self.extra_context)

    def post(self, request):
        return redirect('car:list', pk=request.POST['keyword'], page=1)


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
    paginate_by = 9
    ordering = ['update']
    extra_context = {
        'page': 'Car | Update',
        'judul': 'RentCar',
        'penjelasan': 'penjelasan sewa mobil'
    }

    def get_context_data(self, **kwargs):
        if(self.kwargs['pk'].isdigit()):
            self.extra_context['digit'] = 'digit'
        else:
            self.extra_context['digit'] = None

        self.extra_context['pk'] = self.kwargs['pk']
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        if self.kwargs['pk'].isdigit():
            self.queryset = self.model.objects.filter(
                user=int(self.kwargs['pk']))
            self.kwargs.update({
                'pk': self.kwargs['pk']
            })
        elif self.kwargs['pk'] != 'all':
            self.queryset = self.model.objects.filter(
                tipe__iexact=self.kwargs['pk'])
            self.kwargs.update({
                'pk': self.kwargs['pk']
            })
        return super().get_queryset()


class SewaListView(ListView):
    model = Penyewaan
    paginate_by = 20
    ordering = ['tgl_sewa']
    extra_context = {
        'page': 'Car | List',
        'judul': 'RentCar',
        'penjelasan': 'Car Rental for All Your Traveling Needs'
    }

    def get_queryset(self):
        self.queryset = self.model.objects.filter(
            user=self.request.user)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)


class CarDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        car = Car.objects.only('id').get(id=pk).delete()
        return redirect("car:list", pk=request.user.id, page=1)


class CarUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CarForm
    model = Car
    template_name = 'car/create.html'
    extra_context = {
        'page': 'Car | Update',
        'judul': 'RentCar',
        'penjelasan': 'Car Rental for All Your Traveling Needs'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)


class CarCreateView(LoginRequiredMixin, CreateView):
    form_class = CarForm
    template_name = 'car/create.html'
    extra_context = {
        'page': 'Car | Create',
        'judul': 'RentCar',
        'penjelasan': 'Car Rental for All Your Traveling Needs'
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
        'page': 'Car | Detail',
        'judul': 'RentCar',
        'penjelasan': 'Car Rental for All Your Traveling Needs'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)
