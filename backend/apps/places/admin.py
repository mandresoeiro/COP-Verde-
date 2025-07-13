from django.contrib import admin
from apps.places.models import Place, FavoritePlace, Comment


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'sustainability_score',
        'is_accessible', 'supports_local'
    )
    list_filter = ('category', 'is_accessible', 'supports_local')
    search_fields = ('name', 'address', 'description')
    ordering = ['name']

    fieldsets = (
        ('Informações Gerais', {
            'fields': ('name', 'category', 'description', 'address')
        }),
        ('Localização Geográfica', {
            'fields': ('latitude', 'longitude')
        }),
        ('Sustentabilidade e Acessibilidade', {
            'fields': ('sustainability_score', 'is_accessible', 'supports_local')
        }),
        ('Contato e Funcionamento', {
            'fields': ('website', 'phone_number', 'opening_hours')
        }),
        ('Informações de Acessibilidade', {
            'fields': ('accessibility_notes',)
        }),
        ('Imagem e Metadados', {
            'fields': ('image',)
        }),
    )


@admin.register(FavoritePlace)
class FavoritePlaceAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'place__name')
    autocomplete_fields = ['user', 'place']
    readonly_fields = ('created_at',)
    ordering = ['-created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'place', 'rating',
        'user_location', 'is_verified_visitor', 'created_at'
    )
    list_filter = ('rating', 'is_verified_visitor', 'created_at')
    search_fields = ('user__username', 'place__name', 'text', 'user_location')
    autocomplete_fields = ['user', 'place']
    readonly_fields = ('created_at', 'user')
    ordering = ['-created_at']
