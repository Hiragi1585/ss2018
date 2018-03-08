from django.contrib import admin
from .models import User,Event,LineUser
#from . import User,Event
# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(LineUser)