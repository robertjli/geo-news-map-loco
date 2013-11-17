from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geonewsloco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'maploco.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^maploco/', include('maploco.urls')),
)
