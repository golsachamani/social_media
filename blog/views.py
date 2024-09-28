from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed,HttpResponseBadRequest
from . models import Post
from .import forms
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',context={'posts': posts})

def post(request):  
    if request.method == 'POST':
        form = forms.Post(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.user = request.user
            post.save()
    return redirect('home')
           
            
   
# def post(request):
#     if request.method not in (['POST','post']):
#         return HttpResponseNotAllowed(['you can not post with get method'])
#     user = request.user
#     if not user.id:
#         return HttpresponseBadrequest('you have to login first')
#     content = request.Post.get('content')
#     post = models.Post(user,content)
#     post.save()
#     return redirect('home')
           