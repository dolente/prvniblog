"""mysite URL Configuration

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
from django.conf.urls import url, include #ten include jsme sem taky naimportovali
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls), #ta stříška funguje ve smyslu "musí to začínat", tzn. musí to začínat "admin"
    url(r'', include('blog.urls')), #tohle jsme sem přidali, znamená to vše co nezačíná admin čerpej ze souboru urls.py z adr. Blog
]
