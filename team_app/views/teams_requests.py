
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Team, Request, Member
from ..serializers import RequestSerializer, RequestPostSerializzer


class TeamRequestListCreate(APIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def get(self, request, pk):
        requests = Request.objects.filter(team=pk)
        serializer = RequestSerializer(requests, many=True)

        # Check if team exists
        try:
            team = Team.objects.get(id=pk)
        except:
            return Response(
                {"error": "team doesn't exist"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Get requests to team
        if not requests:
            return Response(
                {"error": "no requests yet"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, pk):
        # Validate input
        serializer = RequestPostSerializzer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get input
        member_id = request.data['member']
        team_id = pk

        # Get member and team objects
        member = Member.objects.get(id=member_id)
        team = Team.objects.get(id=team_id)

        # Check to make sure request for the same member and team doesn't exist already
        request = Request.objects.filter(member=member, team=team)
        if request:
            return Response(
                {'error:': f"{member.member_name}'s request to team {team.team_name} already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Check to make sure member isn't already in the team
        for memb in team.members.values_list():
            if memb[0] == int(member_id):
                return Response(
                    {'error:': f"{member.member_name} is already in team {team.team_name}"}, status=status.HTTP_400_BAD_REQUEST
                )

        Request.objects.create(member=member, team=team)

        return Response(
            {'result': f"{member.member_name}'s request to team {team.team_name} added"}, status=status.HTTP_200_OK
        )
