from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_image', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('list_post', args=[self.id])

    def get_like_url(self):
        return reverse('like_post', args=[self.id])

    def get_dislike_url(self):
        return reverse('dislike_post', args=[self.id])



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)


class DisLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
