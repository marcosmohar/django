from django.conf.urls import url
from .views import index, home, repositories


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^github/', repositories, name='repositories'),
    url(r'^github/(?P<subject>\w+)/$', repositories, name='repositories')
]