from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_auth.models import CustomUser


# Register the user.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    In this class first we import the customuser model that are build
    using the auth.user model that have fields like fname,lname,usename,
    email etc so we add image field to that model using the fieldset.
    """

    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("image",)}),)
