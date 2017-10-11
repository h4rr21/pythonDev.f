from django.conf.urls import url
from .views import LugaresApi, PersonasInLugaresApi

urlpatterns = [
    url(r'/personasLugares', PersonasInLugaresApi.as_view()),
    url(r'^$', LugaresApi.as_view())
]
