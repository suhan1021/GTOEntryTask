from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'developersite'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/developersite'}, name='logout'),
    url(r'^(?P<developer_id>[0-9]+)/edit/$', views.edit, name='edit'),
]
