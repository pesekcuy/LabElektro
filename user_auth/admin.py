from django.contrib import admin
from .models import User

class DataUser(admin. ModelAdmin):
    list_display = ('email', 'year', 'first_name', 'last_name')

# Register your models here.
admin.site.register(User, DataUser)
