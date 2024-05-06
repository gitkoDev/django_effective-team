from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Team, Request
from ..serializers import RequestPostSerializer, RequestGetSerializer


class TeamRequestListCreate(APIView):
    serializer_class = RequestPostSerializer

    def get(self, request, pk):
        queryset = Request.objects.filter(team=pk)
        serializer = RequestGetSerializer(queryset, many=True)

        try:
            Team.objects.get(id=pk)
        except:
            return Response(
                {"error": "team doesn't exist"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Get requests to team
        if not queryset:
            return Response(
                {"error": "no requests yet"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, pk):
        serializer = RequestPostSerializer(
            data=dict(team=pk, member=request.data['member']))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data, status=status.HTTP_200_OK
        )
