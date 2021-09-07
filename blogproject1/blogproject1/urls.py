"""blogproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from testapp import views
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home_view),
    path('post/',views.post_list_view),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',views.detail_list_view,name='post_detail'),
    url(r'^(?P<id>\d+)/$',views.mail_send_view),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    path('sign/', views.sign_up_view),
    path('logout/', views.logout_view),
    path('jobs/',views.jobs_view),
    path('hyd/',views.hyd_jobs_view),
    path('chennai/',views.pune_jobs_view),
    path('blore/',views.chennai_jobs_view),
    path('pune/',views.blore_jobs_view),
    path('movies/',views.index_view),
    path('movie/',views.add_movie_view),
    path('list/',views.list_view),
    path('feedback/',views.feedback_view),
    path('thankyou/',views.thankyou_view),
]
