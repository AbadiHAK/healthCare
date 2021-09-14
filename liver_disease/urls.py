from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='liverForm'),
    path('kindy_pre/',views.liver_pre,name='liverpredicition')
]