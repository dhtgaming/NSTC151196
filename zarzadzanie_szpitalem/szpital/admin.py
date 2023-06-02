from django.contrib import admin
from.models import Pacjent,Doktor,Spotkanie

# Register your models here.
admin.site.register(Doktor)
admin.site.register(Pacjent)
admin.site.register(Spotkanie)