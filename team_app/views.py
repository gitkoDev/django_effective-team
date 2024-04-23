from django.http import HttpResponse
from rest_framework import generics

from .models import (
    Creator,
    Team,
    Member,
    Request
)

from .serializers import (
    CreatorSerializer,
    TeamSerializer,
    MemberSerializer,
    RequestSerializer
)

# List views
class CreatorList(generics.ListCreateAPIView):
    serializer_class = CreatorSerializer
    queryset = Creator.objects.all()
    
class TeamList(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    
class MemberList(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    
class RequestList(generics.ListCreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()


# Detail views 
class CreatorListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreatorSerializer
    queryset = Creator.objects.all()
    lookup_field = 'pk'
    
class TeamListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    lookup_field = 'pk'    

class MemberListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    lookup_field = 'pk'    

class RequestListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
    lookup_field = 'pk'    
 
def index(request):
    return HttpResponse('index page')

