from rest_framework import serializers
from .models import Group, GroupMembership


class GroupSerializer(serializers.ModelSerializer):
    members_count = serializers.IntegerField(source='memberships.count', read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'slug', 'description', 'image_url', 'visibility', 'access_rule', 'required_plan', 'members_count']


class GroupMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembership
        fields = ['id', 'group', 'user', 'role', 'status', 'created_at']
        read_only_fields = ['user', 'status']
