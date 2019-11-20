"""f_django URL Configuration

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

from django.conf.urls import url

from . import views
from django.views.generic import TemplateView


app_name = 'myapp'
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^list$', views.list, name='list'),
    url(r'^Articles/(?P<id>[0-9]+)$', views.details, name='details'),
    url(r'^static/',TemplateView.as_view(template_name='myapp/static.html')),
    #url(r'^connection/',TemplateView.as_view(template_name = 'myapp/login.html')),
    url(r'^login/', views.login, name= 'login'),
    url(r'^profile/',TemplateView.as_view(template_name = 'myapp/profile.html')), 
    url(r'^saved/', views.SaveProfile, name = 'saved'),
    url(r'^connection/',views.formView, name = 'loginform'),
    url(r'^logout/',views.logout, name = 'logout'),

]
