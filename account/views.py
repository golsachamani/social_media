from django.shortcuts import render, redirect
from django.views.generic import base, CreateView,FormView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.http import HttpRequest
from . import forms
# Create your views here.


class Login(base.View):
    template_name = 'registration/login.html'

    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            return redirect('home')
        form = forms.Login()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = forms.Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

        return render(request, 'registration/login.html', context={'form': form})


class Logout(base.View):

    def get(self, request):
        logout(request)
        return redirect('home')

    def post(self, request):
        logout(request)
        return redirect('home')


class Signup(FormView):
    form_class = forms.Signup
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # Save the user to the database
        return super().form_valid(form)
