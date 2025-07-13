from django.db import models
from django.conf import settings  # para o modelo User
from .choices import CATEGORY_CHOICES  # Opções externas para reuso e limpeza


class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome do local")

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name="Categoria"
    )

    description = models.TextField(verbose_name="Descrição")
    address = models.CharField(max_length=300, verbose_name="Endereço")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")

    sustainability_score = models.FloatField(
        help_text="Nota de 0 a 10",
        verbose_name="Índice de Sustentabilidade"
    )

    is_accessible = models.BooleanField(
        default=False,
        verbose_name="Acessível para pessoas com deficiência"
    )

    supports_local = models.BooleanField(
        default=False,
        verbose_name="Iniciativa local"
    )

    image = models.ImageField(
        upload_to='places/',
        blank=True,
        null=True,
        verbose_name="Imagem (opcional)"
    )

    # 🔄 Novos campos úteis ao visitante:
    website = models.URLField(blank=True, null=True, verbose_name="Site oficial")
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="Telefone para contato")
    opening_hours = models.CharField(max_length=100, blank=True, verbose_name="Horário de funcionamento")
    accessibility_notes = models.TextField(blank=True, verbose_name="Observações de acessibilidade")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    class Meta:
        ordering = ['name']
        verbose_name = "Local"
        verbose_name_plural = "Locais"


# 🟢 Relacionamento: locais favoritados por usuários
class FavoritePlace(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name="Local Favoritado"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Adicionado em")

    class Meta:
        unique_together = ['user', 'place']
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"

    def __str__(self):
        return f"{self.user.username} ❤️ {self.place.name}"


# 💬 Comentários com avaliação e contexto do visitante
class Comment(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Local"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )
    text = models.TextField(verbose_name="Comentário")
    rating = models.PositiveIntegerField(default=5, verbose_name="Nota (1 a 10)")
    image = models.ImageField(
        upload_to="comments/",
        blank=True,
        null=True,
        verbose_name="Foto do visitante (opcional)"
    )
    user_location = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Cidade/Estado do visitante"
    )
    is_verified_visitor = models.BooleanField(
        default=False,
        verbose_name="Visitante verificado"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __str__(self):
        return f"{self.user.username} - {self.rating}/10"
