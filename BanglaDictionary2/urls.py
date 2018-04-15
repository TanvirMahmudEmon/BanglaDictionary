"""BanglaDictionary2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dictionarys/', include('Dictionary.urls')),  # video: 4
    url(r'^quiz/', include('quiz.urls')),
    # individual url ie: multichoice, essay, true_false can be set by the admin from admin panel
    url(r'^myblog/', include('myblog.urls')),

    #user auth urls # For Video No: 9
    url(r'^accounts/login/$', 'BanglaDictionary2.views.login'), # For Video No: 9
    url(r'^accounts/auth/$', 'BanglaDictionary2.views.auth_view'), # For Video No: 9
    url(r'^accounts/logout/$', 'BanglaDictionary2.views.logout'), # For Video No: 9
    url(r'^accounts/loggedin/$', 'BanglaDictionary2.views.loggedin'), # For Video No: 9
    url(r'^accounts/invalid/$', 'BanglaDictionary2.views.invalid_login'), # For Video No: 9

    url(r'^accounts/register/$', 'BanglaDictionary2.views.register_user'), # For Video No: 10
    url(r'^accounts/register_success/$', 'BanglaDictionary2.views.register_success'), # For Video No: 10
]
