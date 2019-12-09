from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout


class UserFormView(View):
    form_class = UserForm
    template_name = 'auth/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'page': 'register', 'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            if user.is_active:
                login(request, user)
                return redirect('car:index')
        return redirect('auth:register')


class LoginView(View):
    template_name = 'auth/login.html'

    def get(self, request):
        return render(request, self.template_name, {'page': 'login'})

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('car:index')
        else:
            return redirect('auth:login')


def LogoutView(request):
    logout(request)
    return redirect('car:index')