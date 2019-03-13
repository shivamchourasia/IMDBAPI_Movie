"""IMDBAPI URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from movies.views import MovieList, MovieDetails, MovieSearch

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/$', MovieList.as_view(), name='Movie_List'),
    url(r'^movies/(?P<pk>[0-9]+)$', MovieDetails.as_view(), name='Movie_Details'),
    url(r'^movies/search$', MovieSearch.as_view(), name='Movie_Search'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)