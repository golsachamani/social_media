from django.shortcuts import render, redirect, reverse
from django.views.generic import (
    base,
    CreateView,
    FormView,
    DetailView,
    UpdateView,
    ListView,
)

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import serializers
from . import models
# Create your views here.


@api_view(["POST"])
def signin(request):
    serializer = serializers.Login(request.data)
    if serializer.is_valid():
        username = serializer.username
        password = serializer.password
        user = authenticate(
            request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# class Login(base.View):
#     template_name = 'registration/login.html'

#     def get(self, request: HttpRequest):
#         if request.user.is_authenticated:
#             return redirect('home')
#         form = forms.Login()
#         return render(request, self.template_name, context={'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('home')
#         form = forms.Login(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(
#                 request=request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')

#         return render(request, 'registration/login.html', context={'form': form})


@api_view(["GET"])
def signout(request):
    logout(request)
    return Response(status=status.HTTP_202_ACCEPTED)

# class Logout(base.View):

#     def get(self, request):
#         logout(request)
#         return redirect('home')

#     def post(self, request):
#         logout(request)
#         return redirect('home')


@api_view(["POST"])
def signup(request):
    serializer = serializers.Signup(request.data)
    if serializer.is_valid():
        user = serializer.save()
        login(request, user)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# class Signup(FormView):
#     form_class = forms.Signup
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         result = super().form_valid(form)
#         user = form.save()
#         login(self.request, user)
#         return redirect(self.success_url)

@api_view(["GET", "POST"])
def profile(request, pk):
    if request.method == "GET":
        p = models.Profile.objects.get(pk=pk)
        serializer = serializers.Profile(p)
        return Response(data=serializer.data)
    elif request.method == "POST":
        serializer = serializers.Profile(request.data)
        if serializer.is_valid():
            profile = serializer.save(commit=False)
            profile.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = models.Profile
    template_name = 'account/profile_detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        # Get the existing context
        context = super().get_context_data(**kwargs)

        profile = self.get_object()  # Get the Profile object

        # Check if the logged-in user's profile is following the profile being viewed
        logged_in_user_profile = self.request.user.profile
        is_following = models.Follow.objects.filter(
            follower=logged_in_user_profile, followed=profile).exists()

        # Add follow status to the context
        context['is_following'] = is_following

        return context
    # This method is used to get the profile of the currently logged-in user
    # Automatically create a profile if it doesn't exist

    # def get_object(self):
    #     profile, created = models.Profile.objects.get_or_create(
    #         user=self.request.user)
    #     return profile
    #   return models.Profile.objects.get(user=self.request.user)


# class UpdateProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     form_class = forms.Profile
#     template_name = 'account/update_profile.html'
#     context_object_name = 'profile'

#     def get_success_url(self):
#         return reverse('profile_detail', args=[self.kwargs['pk']])
#  # Automatically fetch the object to update using 'pk' from the URL
#     # Override the get_object method to fetch or create the profile

#     def get_object(self, queryset=None):
#         # Use 'username' if needed
#         return models.Profile.objects.get(pk=self.kwargs['pk'])

#     def test_func(self):
#         obj = self.get_object()
#         return obj.user == self.request.user

@api_view(["GET"])
def follow(request, pk):
    followed_profile = get_object_or_404(models.Profile, pk=pk)
    if request.user.profile != followed_profile:
        models.Follow.objects.get_or_create(
            follower=request.user.profile, followed=followed_profile
        )
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
# @login_required
# def follow(request, pk):
#     followed_profile = get_object_or_404(models.Profile, pk=pk)
#     if request.user.profile != followed_profile:
#         models.Follow.objects.get_or_create(
#             follower=request.user.profile, followed=followed_profile)
#     return redirect(reverse('profile_detail', args=[pk]))


@api_view(["GET"])
def unfollow(request, pk):
    followed_profile = get_object_or_404(models.Profile, pk=pk)
    follow_relation = models.Follow.objects.filter(
        follower=request.user.profile, followed=followed_profile
    )
    if follow_relation.exists():
        follow_relation.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# @login_required
# def unfollow(request, pk):
#     followed_profile = get_object_or_404(models.Profile, pk=pk)
#     follow_relation = models.Follow.objects.filter(
#         follower=request.user.profile, followed=followed_profile)
#     if follow_relation.exists():
#         follow_relation.delete()
#     return redirect(reverse('profile_detail', args=[pk]))
