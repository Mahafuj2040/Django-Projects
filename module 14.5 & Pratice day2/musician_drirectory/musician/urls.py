from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_musician, name='add_musician'),
    path('delete/<int:id>/', views.musician_delete, name='musician_delete'),
    path('edit/<int:id>/', views.musician_edit, name='musician_edit'),
]
