"""api_tab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from testapi import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tag_home/', views.index, name='tag_home'),
    path('beanstalk_home/', views.beanstalk_home, name='beanstalk_home'),
    path('beanstalk_api/', views.beanstalk_quote, name='beanstalk_exe'),
    path('beanstalk_policy/', views.beanstalk_policy, name='beanstalk_exe2'),
    path('beanstalk_amendment/', views.beanstalk_policy, name='beanstalk_amendment'),
    path('test_execution/', views.beanstalk_quote, name='test_execution'),
]
