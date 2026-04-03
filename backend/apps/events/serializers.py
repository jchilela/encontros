from rest_framework import serializers
from .models import Event, RSVP


class EventSerializer(serializers.ModelSerializer):
    confirmed_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'slug', 'summary', 'description', 'image_url', 'event_format', 'visibility', 'required_plan', 'starts_at', 'ends_at', 'timezone', 'venue_name', 'address_line', 'online_url', 'capacity', 'base_currency', 'status', 'confirmed_count']

    def get_confirmed_count(self, obj):
        return obj.rsvps.filter(status='confirmed').count()


class RSVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSVP
        fields = ['id', 'event', 'user', 'status', 'checked_in_at', 'created_at']
        read_only_fields = ['user', 'checked_in_at']
