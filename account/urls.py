from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    # path('profile/<int:pk>/update/', views.UpdateProfile.as_view(), name='update_profile'),
    path('profile/<int:pk>/follow/', views.follow, name='follow_profile'),
    path('profile/<int:pk>/unfollow/', views.unfollow, name='unfollow_profile'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
