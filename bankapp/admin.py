from django.contrib import admin

# Register your models here.
from bankapp.models import City, District, Register

admin.site.register(City)
admin.site.register(District)
admin.site.register(Register)
