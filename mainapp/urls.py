"""abris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.index, name='index'),
    re_path(r'^draw-add/$', mainapp.draw_add, name='draw_add'),
    re_path(r'^draw/(?P<pk>\d+)/$', mainapp.draw_read, name='draw'),
    re_path(r'^draw-delete/(?P<pk>\d+)/$', mainapp.draw_delete, name='draw_delete'),
    re_path(r'^draw-update/(?P<pk>\d+)/$', mainapp.draw_update, name='draw_update'),
    # re_path(r'^draw-update/(?P<pk>\d+)/?coordinates=/$', mainapp.draw_update, name='draw_update'),
]
