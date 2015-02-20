from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import classification.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nonesense.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', classification.views.index, name='index'),
	url(r'^statistics', classification.views.statistics, name='statistics'),
    url(r'^admin/', include(admin.site.urls)),

)
