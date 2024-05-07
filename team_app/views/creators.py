from rest_framework import generics

from team_app.models import Creator
from team_app.serializers import CreatorSerializer


class CreatorListCreate(generics.ListCreateAPIView):
    serializer_class = CreatorSerializer
    queryset = Creator.objects.all()


class CreatorListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreatorSerializer
    queryset = Creator.objects.all()
    lookup_field = 'pk'
