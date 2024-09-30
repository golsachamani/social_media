from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/create/', views.CreateProfile.as_view(), name='create_profile'),
    path('profile/update/', views.UpdateProfile.as_view(), name='update_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
