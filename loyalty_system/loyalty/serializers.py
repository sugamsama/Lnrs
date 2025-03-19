from rest_framework import serializers
from .models import LoyaltyProgram

class LoyaltyProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyProgram
        fields = ['id', 'user_id', 'last_updated', 'points']
        