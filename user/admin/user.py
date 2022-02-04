from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from ..forms import UserCreationForm, UserChangeForm
from ..models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('phone', 'is_superuser', 'is_superuser', 'is_active', 'is_staff',)
    list_filter = ('phone', 'is_superuser', 'is_superuser', 'is_active', 'is_staff', "user_permissions", "questions")
    fieldsets = (
        ("INFO", {'fields': ('phone', 'password', 'profile', 'is_superuser', 'is_active', 'is_staff',)}),
        ("AUTHENTICATION AND AUTHORIZATION", {'fields': ("groups", "user_permissions",)}),
        ("Questionnaire", {'fields': ("score", "questions")}),

    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', ),
        }),
    )
    search_fields = ('phone',)
    ordering = ('phone',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
