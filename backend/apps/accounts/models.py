from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('visitor', 'Visitante'),
        ('researcher', 'Pesquisador'),
        ('manager', 'Gestor Público'),
        ('guide', 'Guia Turístico'),
        ('admin', 'Administrador'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='visitor',
        verbose_name='Tipo de usuário'
    )

    organization = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Organização ou Instituição'
    )

    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name='Biografia ou função'
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
