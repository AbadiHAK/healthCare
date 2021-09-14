"""healthCareProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import diabetes
import cancer
import heart_disease
import kindy_disease
import liver_disease

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('home.urls')),
    path('home/',include('home.urls')),
    path('cancer/' , include('cancer.urls')),
    path('cancer_pre/', cancer.views.cancer_pre, name='cancerprediction'),
    path('diabetes/' , include('diabetes.urls')),
    path('diabetes_pre/',diabetes.views.diabetes_pre, name='diabetesprediction'),
    path('heart/', include('heart_disease.urls')),
    path('heart_pre/',heart_disease.views.heart_pre,name='heaertpredicition'),
    path('kindy/', include('kindy_disease.urls')),
    path('kindy_pre/',kindy_disease.views.kindy_pre,name='kindypredicition'),
    path('liver/', include('liver_disease.urls')),
    path('liver_pre/',liver_disease.views.liver_pre,name='liverpredicition'),




    
]
