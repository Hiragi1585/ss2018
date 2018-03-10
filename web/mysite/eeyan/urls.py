from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path("<int:event_id>/detail",views.detail,name="detail"),
    path("<int:user_id>/provider",views.provider,name="provider"),
    path("login/",views.loginForm,name="loginForm"),
]