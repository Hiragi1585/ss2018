from django.urls import include,path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("form/",views.form,name="form"),
    path("<int:user_id>/event/",views.event,name="event"),
    path("<int:user_id>/modify/",views.modify,name="modify"),
    path("<int:event_id>/detail/",views.detail,name="detail"),
    path("<int:user_id>/eventList/",views.eventList,name="eventList"),
    path("receive/",views.receive,name="receive"),
]