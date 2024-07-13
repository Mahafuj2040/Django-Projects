from django.urls import path
from . import views

urlpatterns = [
    path('musician/add/', views.MusicianCreateView.as_view(), name='add_musician'),
    path('musician/delete/<int:pk>/', views.MusicianDeleteView.as_view(), name='musician_delete'),
    path('musician/edit/<int:pk>/', views.MusicianUpdateView.as_view(), name='musician_edit'),
    path('', views.MusicianListView.as_view(), name="homepage"),
]
