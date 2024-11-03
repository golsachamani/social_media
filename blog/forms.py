from django.forms import ModelForm
from . models import Post
from tinymce.widgets import TinyMCE
class Post(ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        # widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}

