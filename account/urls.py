from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.reg_success, name='reg_success'),
    url(r'^login/success/$', views.login_success, name='login_success'),
]

