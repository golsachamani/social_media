from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/',views.Signup.as_view(),name = 'signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
