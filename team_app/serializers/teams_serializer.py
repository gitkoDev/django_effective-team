from rest_framework import serializers
from .members_serializer import MemberSerializer

from ..models import Team


class TeamSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('__all__')
