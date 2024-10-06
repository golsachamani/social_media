from django.shortcuts import render, redirect
from django.views.generic import base, CreateView, FormView, DetailView, UpdateView, ListView

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpRequest
from . import forms
from . import models
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
        result = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class ProfileListView(ListView):
    model = models.Profile
    template_name = 'account/profile_list'
    context_object_name = 'profiles'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = models.Profile
    template_name = 'account/profile_detail.html'
    context_object_name = 'profile'
    # This method is used to get the profile of the currently logged-in user
    # Automatically create a profile if it doesn't exist

    # def get_object(self):
    #     profile, created = models.Profile.objects.get_or_create(
    #         user=self.request.user)
    #     return profile
    #   return models.Profile.objects.get(user=self.request.user)


class UpdateProfile(LoginRequiredMixin, UpdateView):
    form_class = forms.Profile
    template_name = 'account/update_profile.html'
    success_url = reverse_lazy('profile')
    # Override the get_object method to fetch or create the profile

 # Automatically fetch the object to update using 'pk' from the URL
    def get_object(self, queryset=None):
        # Use 'username' if needed
        return models.Profile.objects.get(pk=self.kwargs['pk'])
