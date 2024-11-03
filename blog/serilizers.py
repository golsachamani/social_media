from rest_framework.serializers import ModelSerializer
from . import models


class Post(ModelSerializer):
    class Meta:
        model = models.Post
        fields = "__all__"


class Like(ModelSerializer):
    class Meta:
        model = models.Like
        fields = "__all__"


class DisLike(ModelSerializer):
    class Meta:
        model = models.DisLike
        fields = "__all__"
