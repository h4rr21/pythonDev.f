from django.conf.urls import url
from .views import PersonasApi, PersonaApi

urlpatterns = [
    url(r'^$', PersonasApi.as_view(), name="personas_end_point"),
    url(r'(?P<pk>[0-9]+)/$', PersonaApi.as_view(), name="persona_end_point")
]
