
from django.contrib import admin
from django.conf.urls import url
from Saludo.views import HolaMundo
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HolaMundo),
]
