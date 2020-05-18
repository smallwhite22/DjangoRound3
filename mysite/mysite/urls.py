"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from polls.views import hello3, sayhello, hello4



'''from django.conf.urls import url
from polls.views import sayhello'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', sayhello),
    path('hello3/<str:username>/', hello3),
    path('hello4/<str:username>/', hello4),


    #　url(r'^$', sayhello),
    # 二種方式，可能新版不再用，需再釐清
]

