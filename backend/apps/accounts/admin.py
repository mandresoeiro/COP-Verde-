from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Campos exibidos na listagem do admin
    list_display = ('username', 'email', 'role', 'organization', 'is_staff')

    # Permite filtro lateral por esses campos
    list_filter = ('role', 'is_staff', 'is_superuser')

    # Campos exibidos ao editar/criar usuário no admin
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informações do COP Verde', {
            'fields': ('role', 'organization', 'bio'),
        }),
    )

    # Campos exibidos ao criar novo usuário no admin
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Informações do COP Verde', {
            'fields': ('role', 'organization', 'bio'),
        }),
    )

    search_fields = ('username', 'email', 'organization')
    ordering = ('username',)
