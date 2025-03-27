from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    # afficher les champs dans le datagridview et filtrer les elments selon son choix
    list_display=('id','email','name','is_active','staff')
    list_filter=('is_active','staff')
    
    fieldsets=(
        ('User credentials',{'fields': ('email','password')}),
        ('personnal Info', {'fields': ('name','is_active','staff')})
    )
    
    add_fieldsets=(
        (None, {'classes':('wide',),
                
                'fields': ('email','name','password','password2','is_active','staff')})
    )
    
    search_fields=('email','name')
    ordering=('id','email')
    filter_horizontal=()
    # register your model here
admin.site.register(User, UserModelAdmin)