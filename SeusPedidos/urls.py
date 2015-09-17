from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#from SeusPedidos.App.views.index import *

from SeusPedidos.App.views.index import *

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'SeusPedidos.views.home', name='home'),
    # url(r'^SeusPedidos/', include('SeusPedidos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'$', index.as_view()),
)
