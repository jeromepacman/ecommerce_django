from django.contrib import admin
from users.models import ShippingAddress, Profile
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'last_login']


admin.site.register(User, UserAdmin)
admin.site.register(ShippingAddress)
admin.site.register(Profile)