from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
    path('pass_change/', views.pass_change, name='pass_change'),
    path('logout/', views.user_logout, name='logout'),
    # path('logout/', views.UserLogout.as_view(), name='logout'),
]
