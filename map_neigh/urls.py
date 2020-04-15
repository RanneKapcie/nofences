from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'map_neigh'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url("register/", views.register, name='register'),
    url("logout/", views.logout_request, name='logout'),
    url("login/", views.login_request, name='login'),
    url("add/", views.add_announcement, name='add'),
    url('profile/', views.profile, name='profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html', success_url='done/')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_d.html')),
]
