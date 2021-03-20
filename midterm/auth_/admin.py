from django.contrib import admin
from auth_.models import MainUser


@admin.register(MainUser)
class MainUserAdmin(admin.ModelAdmin):
    list_display = ['email',]
