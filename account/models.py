from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    nikename= models.CharField(max_length=127)
    bio = models.TextField()
    image= models.ImageField(upload_to = 'media/profile_image')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nikename}@{self.user.username}'
    