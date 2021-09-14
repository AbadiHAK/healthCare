from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='kindyForm'),
    path('kindy_pre/',views.kindy_pre,name='kindypredicition')
]