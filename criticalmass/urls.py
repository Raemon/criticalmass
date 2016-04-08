from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import events.views

# Examples:
# url(r'^$', 'criticalmass.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', events.views.index, name='index'),
    url(r'^db', events.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
