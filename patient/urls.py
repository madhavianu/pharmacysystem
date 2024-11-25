from django.urls import path
from . import views

urlpatterns=[
    path('plist/', views.patient_list, name = 'patient_list'),
    path('padd/', views.patient_add, name = 'patient_add'),
    #path('pedit/', views.patient_edit, name = 'patient_edit'),
    path('patient/edit/<int:id>/', views.patient_edit, name='patient_edit'),
    path('patient/delete/<int:id>/', views.patient_delete, name='patient_delete'),
    ]