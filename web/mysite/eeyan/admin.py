from django.contrib import admin
from .models import Event,User,Line,Place
# Register your models here.

admin.site.register(Event)
admin.site.register(Place)
admin.site.register(User)
admin.site.register(Line)


