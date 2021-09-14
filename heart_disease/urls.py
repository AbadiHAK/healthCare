from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='heartDiseaseForm'),
    path('heart_pre/',views.heart_pre,name='heaertpredicition')
]