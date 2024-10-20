from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    list_display=('id', 'email', 'name', 'is_admin', 'staff')
    list_filter=('is_admin', 'staff')

    fieldsets=(
        ('User Credentials', {'fields' : ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'is_active', 'staff')}),
    )

    add_fieldsets=(
        (None, {'classes':('wide',),
                'fields':('email', 'name', 'password', 'password2', 'is_active', 'staff')})
    )

    search_fields=('email', 'name')
    ordering=('id', 'email')
    filter_horizontal=()

# Register your models here.
admin.site.register(User, UserModelAdmin)
