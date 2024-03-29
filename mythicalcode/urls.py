from django.conf.urls import patterns, include, url
from django.contrib import admin
from api.views import router


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
