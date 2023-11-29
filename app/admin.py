from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import Detail

# Register your models here.
admin.site.register(Detail)
