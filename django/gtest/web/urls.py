from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'action',views.action, name='action'),
    url(r'bb',views.test, name='action'),
    url(r'domain',views.Domain, name='action'),
    url(r'finish',views.Finish, name='action'),
]