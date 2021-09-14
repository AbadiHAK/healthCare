from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='cancerForm'),
    path('cancer_pre/', views.cancer_pre, name='cancerprediction'),

]