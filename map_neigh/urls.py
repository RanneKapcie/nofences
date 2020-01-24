from django.conf.urls import url, include
from . import views

app_name = 'map_neigh'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url("register/", views.register, name='register'),
    url("logout/", views.logout_request, name='logout'),
    url("login/", views.login_request, name='login'),
]
