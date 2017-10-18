from django.conf.urls import url
from .views import LugaresApi, PersonasInLugaresApi

urlpatterns = [
    url(r'/personasLugares', PersonasInLugaresApi.as_view(), name="lugares_inPersonas_end_point"),
    url(r'^$', LugaresApi.as_view(), name="lugares_end_point")
]
