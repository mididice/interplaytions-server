from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

import midi.api
import midi.api2

app_name='midi'

router = routers.DefaultRouter() 
router.register(r'midi', midi.api.MemberViewSet, base_name='api')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/doc', get_swagger_view(title='Rest API Document')),
    url(r'^api/v1/', include((router.urls, 'midi'), namespace='api')),
    url(r'^api/v2/', midi.api2.generate_midi),
    url(r'^api/test/', midi.api2.request_midi),
]