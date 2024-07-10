from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.add_albumb, name='add_albumb'),
    path('delete/<int:id>/', views.delete_albumb, name="delete_albumb"),
    path('edit/<int:id>/', views.edit_albumb, name="edit_albumb")
]
