from django.conf.urls.defaults import *
from liveupdate.models import Update

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list',{
        'queryset': Update.objects.all()
    }),
    url(r'^updates-after/(?P<id>\d+)/$',
        'liveupdate.views.updates_after')
)