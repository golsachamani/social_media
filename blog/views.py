from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import models, serilizers
# Create your views here.


def home(request):
    posts = models.Post.objects.filter(replied_to=None)
    if request.user.is_authenticated:
        my_profile = request.user.profile
        followed = account_models.Follow.objects.filter(follower=my_profile)
        followed_profile = [f.followed for f in followed]
        posts = [p for p in posts if p.profile.is_private or p.profile ==
                 my_profile or p.profile in followed_profile]

    else:
        posts = [p for p in posts if p.profile.is_private]

    form = forms.Post()
    return render(request, 'home.html', context={'posts': posts, 'post_form': form, })


@api_view(["GET", "POST"])
def post(request, pk):
    if request.method == "GET":
        post = models.Post.objects.get(pk=pk)
        serilizer = serilizers.Post(post)
        return Response(serilizer.data)

    elif request.method == "POST":
        replied_to: models.Post = None
        if pk != 0:
            replied_to = models.Post.objects.get(pk=pk)
        serilizer = serilizers.Post(data=request.data)
        if serilizer.is_valid():
            post = serilizer.save(commit=False)
            post.profile = request.user.profile
            post.replied_to = replied_to
            post.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# def post(request, pk):
#     replied_to: models.Post = None
#     if pk != 0:
#         replied_to = models.Post.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = forms.Post(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.profile = request.user.profile
#             post.replied_to = replied_to
#             post.save()
#     return redirect('home')


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

@api_view(["GET"])
def posts(request):
    all_posts = models.Post.objects.filter(replied_to=None)
    serilizer = serilizers.Post(all_posts, many=True)
    return Response(data=serilizer.data)


@api_view(["GET"])
def like_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    profile = request.user.profile
    # Toggle like
    like, created = models.Like.objects.get_or_create(
        post=post, profile=profile)
    if not created:  # If the like already exists, remove it
        like.delete()

    # Remove dislike if it exists
    models.DisLike.objects.filter(post=post, profile=profile).delete()

    return Response(status=status.HTTP_201_CREATED)
# @login_required
# def like_post(request, pk):
#     post = get_object_or_404(models.Post, pk=pk)
#     profile = request.user.profile
#   # Toggle like
#     like, created = models.Like.objects.get_or_create(
#         post=post, profile=profile)
#     if not created:  # If the like already exists, remove it
#         like.delete()

#     # Remove dislike if it exists
#     models.DisLike.objects.filter(post=post, profile=profile).delete()

#     return redirect('home')


# @login_required
# def dislike_post(request, pk):
#     post = get_object_or_404(models.Post, pk=pk)
#     profile = request.user.profile

#     # Toggle dislike
#     dislike, created = models.DisLike.objects.get_or_create(
#         post=post, profile=profile)
#     if not created:  # If the dislike already exists, remove it
#         dislike.delete()

#     # Remove like if it exists
#     models.Like.objects.filter(post=post, profile=profile).delete()

#     return redirect('home')


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
@api_view(["GET"])
def dislike_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    profile = request.user.profile

    # Toggle dislike
    dislike, created = models.DisLike.objects.get_or_create(
        post=post, profile=profile)
    if not created:  # If the dislike already exists, remove it
        dislike.delete()

    # Remove like if it exists
    models.Like.objects.filter(post=post, profile=profile).delete()

    return Response(status=status.HTTP_201_CREATED)
# @login_required
# def dislike_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)pu
#     user = request.user

#     # Check if the user has liked the post before, and if so, remove it
#     if Like.objects.filter(post=post, user=user).exists():
#         Like.objects.filter(post=post, user=user).delete()

#     # If the user hasn't already disliked the post, dislike it
#     if not Dislike.objects.filter(post=post, user=user).exists():
#         Dislike.objects.create(post=post, user=user)

#     return redirect('post_detail', pk=pk)
