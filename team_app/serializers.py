from rest_framework import serializers
from .models import (
    Creator,
    Team,
    Member,
    Request,
    Transaction
)

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ('__all__')
        
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('__all__')
        
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('__all__')
        
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('__all__')
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('__all__')