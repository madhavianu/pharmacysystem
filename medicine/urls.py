from django.urls import path
from . import views

urlpatterns = [
    path('medilist/', views.medi_list, name='medi_list'),
    path('mediadd/', views.medi_add, name='medi_add'),
    path('mediedit/<int:pk>/', views.medi_edit, name='medi_edit'),
    path('medidelete/<int:pk>/', views.medi_delete, name='medi_delete'),
]
