from django.conf.urls import url
from . import views
from account import views as login_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
