from rest_framework import serializers
from . import models


class Profile(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = "__all__"


class Login(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()


class Signup(serializers.ModelSerializer):
    username = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def save(self, **kwargs):
        user = models.User.objects.create_user(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password1"],
            **kwargs,
        )
        return user


class Follow(serializers.ModelSerializer):
    class Meta:
        model = models.Follow
        fields = "__all__"
