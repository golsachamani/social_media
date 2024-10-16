from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('profile/', views.ProfileListView.as_view(),name ='profile'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', views.UpdateProfile.as_view(), name='update_profile'),
    path('profile/<int:pk>/follow/', views.follow, name='follow_profile'),
    path('profile/<int:pk>/unfollow/', views.unfollow, name='unfollow_profile'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
