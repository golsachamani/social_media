from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django .views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .import forms, models
# Create your views here.


def home(request):
    posts = models.Post.objects.filter(replied_to=None)
    return render(request, 'home.html', context={'posts': posts })


def post(request,pk):
    replied_to:models.Post=None
    if pk!=0:
        replied_to= models.Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.Post(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.replied_to = replied_to
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
@login_required
def like_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    user = request.user
  # Toggle like
    like, created = models.Like.objects.get_or_create(post=post, user=user)
    if not created:  # If the like already exists, remove it
        like.delete()

    # Remove dislike if it exists
    models.DisLike.objects.filter(post=post, user=user).delete()

    return redirect('home')


   

@login_required
def dislike_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    user = request.user

      # Toggle dislike
    dislike, created = models.DisLike.objects.get_or_create(post=post, user=user)
    if not created:  # If the dislike already exists, remove it
        dislike.delete()

    # Remove like if it exists
    models.Like.objects.filter(post=post, user=user).delete()

    return redirect('home')














# @login_required
# def like_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     user = request.user

#     # Check if the user has disliked the post before, and if so, remove it
#     if Dislike.objects.filter(post=post, user=user).exists():
#         Dislike.objects.filter(post=post, user=user).delete()

#     # If the user hasn't already liked the post, like it
#     if not Like.objects.filter(post=post, user=user).exists():
#         Like.objects.create(post=post, user=user)

#     return redirect('post_detail', pk=pk)

# @login_required
# def dislike_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     user = request.user

#     # Check if the user has liked the post before, and if so, remove it
#     if Like.objects.filter(post=post, user=user).exists():
#         Like.objects.filter(post=post, user=user).delete()

#     # If the user hasn't already disliked the post, dislike it
#     if not Dislike.objects.filter(post=post, user=user).exists():
#         Dislike.objects.create(post=post, user=user)

#     return redirect('post_detail', pk=pk)
