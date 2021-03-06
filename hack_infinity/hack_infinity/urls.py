"""hack_infinity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.register),
    url(r'^login/', views.login_app),
    url(r'^$',views.index),
    url(r'^logout/',views.logout_app),
    url(r'^add-produce/$', views.add_produce),
    url(r'^market/$', views.market),
    url(r'^add-support/$', views.add_support),
    url(r'^view-support/$', views.view_support),
    url(r'^remove_produce/$', views.remove_produce),
    url(r'^feedback/$', views.feedback),
    url(r'^market/$', views.market),
    url(r'^predictions/$', views.predictions),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
