from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.AlbumbCreate.as_view(), name='add_albumb'),
    path('delete/<int:id>/', views.delete_albumb, name="delete_albumb"),
    path('edit/<int:pk>/', views.AlbumbUpdate.as_view(), name="edit_albumb")
]
