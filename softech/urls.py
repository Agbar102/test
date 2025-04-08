"""
URL configuration for softech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
# from items.views import get_category, about, base
from softech.front import front_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', get_category, name='category'),
    # path('about/', about, name='about'),
    # path('base/', base, name='base'),
    # # path('company/', company, name='company'),

]
if settings.DEBUG:
    urlpatterns += front_urlpatterns

