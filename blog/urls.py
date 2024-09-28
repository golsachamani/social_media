
from django.urls import path
# from .views import home,post_list
from . import views
urlpatterns = [
   path('',views.home,name = 'home'),
   path('post/',views.post,name= 'post'),
]