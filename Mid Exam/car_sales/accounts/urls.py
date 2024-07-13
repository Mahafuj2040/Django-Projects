from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('pass_change/', views.pass_change, name="passwordchange"),
    path('change_data/', views.change_data, name="change_data"),
    
]