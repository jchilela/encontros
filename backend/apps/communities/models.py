from django.conf import settings
from django.db import models
from apps.common.models import TimeStampedModel
from apps.taxonomy.models import Category, City


class Group(TimeStampedModel):
    VISIBILITY_CHOICES = [('public', 'Público'), ('private', 'Privado')]
    ACCESS_CHOICES = [('open', 'Livre'), ('approval', 'Aprovação')]
    PLAN_CHOICES = [('none', 'Sem restrição'), ('free', 'Gratuito'), ('silver', 'Silver'), ('gold', 'Gold')]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_groups')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=180)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    visibility = models.CharField(max_length=32, choices=VISIBILITY_CHOICES, default='public')
    access_rule = models.CharField(max_length=32, choices=ACCESS_CHOICES, default='open')
    required_plan = models.CharField(max_length=32, choices=PLAN_CHOICES, default='none')
    rules = models.TextField(blank=True)


class GroupMembership(TimeStampedModel):
    ROLE_CHOICES = [('member', 'Membro'), ('coorganizer', 'Coorganizador'), ('moderator', 'Moderador')]
    STATUS_CHOICES = [('pending', 'Pendente'), ('active', 'Ativo'), ('rejected', 'Rejeitado'), ('removed', 'Removido')]

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='memberships')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='group_memberships')
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='member')
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='active')

    class Meta:
        unique_together = ('group', 'user')
