from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.common.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    ROLE_CHOICES = [
        ('member', 'Membro'),
        ('organizer', 'Organizador'),
        ('coorganizer', 'Coorganizador'),
        ('moderator', 'Moderador'),
        ('support', 'Suporte'),
        ('admin', 'Administrador'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='member')
    phone = models.CharField(max_length=32, blank=True)
    is_email_verified = models.BooleanField(default=False)
    is_identity_verified = models.BooleanField(default=False)
    preferred_currency = models.CharField(max_length=8, default='EUR')
    timezone = models.CharField(max_length=64, default='Europe/Lisbon')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Profile(TimeStampedModel):
    PRIVACY_CHOICES = [('public', 'Público'), ('members', 'Membros'), ('private', 'Privado')]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=120, blank=True)
    language_code = models.CharField(max_length=12, default='pt')
    interests = models.JSONField(default=list, blank=True)
    notification_preferences = models.JSONField(default=dict, blank=True)
    privacy_level = models.CharField(max_length=32, choices=PRIVACY_CHOICES, default='public')
