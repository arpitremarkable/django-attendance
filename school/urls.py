from django.conf.urls import patterns, include, url

from school import api
from tastypie.api import Api

from django.contrib import admin
admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(api.UserResource())
v1_api.register(api.AttendanceResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
