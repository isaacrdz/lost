from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

from .views import (
    PersonList,
    PersonDetail,
    PersonCreation,
    PersonUpdate,
    PersonDelete,
   )

urlpatterns = [
	url(r'^login/$', views.auth_login, name='authentication'),	
    url(r'^logout$', auth_views.logout, {'next_page': '/persons'}, name='logout'),
    url(r'^$', PersonList.as_view(), name='list'),
    url(r'^nuevo$', PersonCreation.as_view(), name='new'),
    url(r'^(?P<pk>\d+)$', PersonDetail.as_view(), name='detail'),
    url(r'^editar/(?P<pk>\d+)$', PersonUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', PersonDelete.as_view(), name='delete'),



       
]