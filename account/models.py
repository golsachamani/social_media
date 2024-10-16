from django.db import models
from django.contrib.auth.models import User
from django .shortcuts import reverse
# Create your models here.
class Profile(models.Model):
    nikename= models.CharField(max_length=127)
    bio = models.TextField()
    image= models.ImageField(upload_to = 'profile_image/',blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nikename}@{self.user.username}'
    def get_absolute_url(self):
        return reverse('profile_detail' , args=[self.id])

class Follow(models.Model):
    follower= models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='following')
    followed =models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    
    