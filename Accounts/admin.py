from django.contrib import admin
from .models import new_user
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = new_user
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name','last_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name','last_name',
                    'is_active', 'is_staff','is_confirmed')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_confirmed')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name','last_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(new_user, UserAdminConfig)