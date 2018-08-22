"""cheetahfc URL Configuration

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
from website import views

# for hosting imports
from django.conf.urls import url

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('ceo-message', views.ceoMessage, name='ceo-message'),
#     path('technical-team', views.techTeam, name='technical-team'),
#     path('first-team', views.firstTeam, name='first-team'),
#     path('under-17', views.u17, name='under-17'),
#     path('under-15', views.u15, name='under-15'),
#     path('under-13', views.u13, name='under-13'),
#     path('news', views.news, name='news'),
#     path('news-details/<int:news_id>/', views.news_details, name='news_details'),
#     path('fixtures', views.fixtures, name='fixtures'),
#     path('players-abroad', views.playersAbroad, name='players-abroad'),
#     path('gallery', views.gallery, name='gallery')
# ]

"""
 Hosting configurations for the urls here --> Need a new server for the new configs to work
"""

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^ceo-message/$',views.ceoMessage, name='ceo-message'),
    url(r'^technical-team/$',views.techTeam, name='technical-team'),
    url(r'^first-team/$',views.firstTeam, name='first-team'),
    url(r'^under-17/$',views.u17, name='under-17'),
    url(r'^under-15/$',views.u15, name='under-15'),
    url(r'^under-13/$',views.u13, name='under-13'),
    url(r'^news/$', views.news, name='news'),
    url(r'^news-details/(?P<news_id>\d+)/$', views.news_details, name='news_details'),
    url(r'^fixtures/$',views.fixtures, name='fixtures'),
    url(r'^players-abroad/$',views.playersAbroad, name='players-abroad'),
    url(r'^gallery/$',views.gallery, name='gallery')
]
