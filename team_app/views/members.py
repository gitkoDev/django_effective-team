from rest_framework import generics, status
from rest_framework.response import Response

from ..models import Member
from ..serializers import MemberSerializer


class MemberListCreate(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    def get(self, request):
        members = Member.objects.all().order_by('stamina')
        serializer = MemberSerializer(members, many=True)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )


class MemberListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    lookup_field = 'pk'
