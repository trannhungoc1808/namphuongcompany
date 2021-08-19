"""newsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from theme.views import homepage
from theme.views import contact #1
from django.urls import path
from . import index

urlpatterns = [
    #url(r'^admin/', admin.site.urls), #2
    #url(r'^$', homepage) #3
    path('',index.home,name='home'),
    path('basevietnamese/',index.homevietnamese,name='homevietnamese'),
    path('baseenglish/', index.homeenglish,name='homeenglish'),
    path('Products-details/',index.specialpomelo,name='specialpomelo'),
    path('Products-details2/',index.pomelotype1,name='pomelotype1'),
    path('Products-details3/',index.pomelotype2,name='pomelotype2'),
    path('Products-details-Vie/',index.pdetailsvie,name='pdetailsvie'),
    path('Products-details2-Vie/',index.pdetails2vie,name='pdetails2vie'),
    path('Products-details3-Vie/',index.pdetails3vie,name='pdetails3vie'),
    path('Transport-Vie/',index.transportvie,name='transportvie'),
    path('Transport/',index.transport,name='transport'),
    #path('contact/',index.contact,name='contact'),
]
