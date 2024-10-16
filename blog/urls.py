
from django.urls import path
# from .views import home,post_list
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/send/', views.post, name='post'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/<int:pk>/dislike/', views.dislike_post, name='dislike_post'),

]
