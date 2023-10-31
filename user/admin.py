from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

class UserModelAdmin(BaseUserAdmin):
    list_display = ('name', 'email', 'user_type', 'phone')
    list_filter = ('user_type',)
    filter_horizontal = ()
    ordering = ('phone', 'id')
    fieldsets = (
        ('User Credentials', {'fields': ('name', 'email', 'phone', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_superuser','is_staff','user_type', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )



admin.site.register(User, UserModelAdmin)
