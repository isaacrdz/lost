from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
 url(r'^persons/', include('persons.urls', namespace='persons')),
 url(r'^admin/', admin.site.urls),
]