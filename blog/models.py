from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from tinymce import models as tinymce_models
from account import models as account_models


class Post(models.Model):
    content = tinymce_models.HTMLField()
    profile = models.ForeignKey(account_models.Profile, on_delete=models.CASCADE,default=None,null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    replied_to = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)

    def replies(self):
        return Post.objects.filter(replied_to=self.id)

    def get_absolute_url(self):
        return reverse('list_post', args=[self.id])

    def get_like_url(self):
        return reverse('like_post', args=[self.id])

    def get_dislike_url(self):
        return reverse('dislike_post', args=[self.id])

    def get_reply_url(self):
        return reverse('post', args=[self.id])


class Like(models.Model):
    profile = models.ForeignKey(account_models.Profile, on_delete=models.CASCADE,null=True,default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)


class DisLike(models.Model):
    profile = models.ForeignKey(account_models.Profile, on_delete=models.CASCADE,null=True,default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
