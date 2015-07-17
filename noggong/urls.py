from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noggong.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^1/$', 'rdbms.views.sample1'),
    url(r'^2/$', 'rdbms.views.sample2'),
    url(r'^3/$', 'rdbms.views.sample3'),

)
