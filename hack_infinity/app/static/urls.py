"""RegisterMyDevice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from register import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^appLogin/', views.appLogin),
    url(r'^addNewUserApp/',views.addNewUserApp),
    url(r'^addNewDeviceApp/',views.addNewDeviceApp),
    url(r'^login/',views.login_page),
    url(r'^dashboard/',views.dashboard),
    url(r'^logout/',views.logout_app),
    url(r'^register/',views.register),
    url(r'^user_dashboard/',views.user_dashboard),
    url(r'^black_list/',views.black_list),
    url(r'^white_list/',views.white_list),
    url(r'^add_fir/',views.add_fir),
    url(r'^apicall/(\d+)',views.apicall),
    url(r'^add_white_list',views.add_white_list),
]

