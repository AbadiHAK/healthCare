from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='diabetesForm'),
    path('diabetes_pre/', views.diabetes_pre, name='diabetesprediction'),

]