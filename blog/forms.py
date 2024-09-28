from django.forms import ModelForm
from . models import Post

class Post(ModelForm):
    class Meta:
        model = Post
        fields = ['content']