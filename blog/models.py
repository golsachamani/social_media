from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_image',blank=True,null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('list_post', args=[self.id])
