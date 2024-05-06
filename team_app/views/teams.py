from rest_framework import generics

from ..models import Team
from ..serializers import TeamSerializer


class TeamListCreate(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    lookup_field = 'pk'
