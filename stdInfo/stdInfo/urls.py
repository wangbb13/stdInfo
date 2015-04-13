from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import stdInfo.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stdInfo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/', include('student.urls')),
    url(r'^manage/', include('manage.urls')),
    url(r'^postmanage/', include('postmanage.urls')),
    url(r'^$', stdInfo.views.index),
    url(r'^logout/',stdInfo.views.logout),
    url(r'^create_user/p1(\w+)p2(.+)/', stdInfo.views.create_user),
    url(r'^del/', stdInfo.views.del_cookie),
    )
