from django.db.models import Prefetch

from rest_framework import generics, status
from rest_framework.response import Response

from ..models import Request, Member, Team
from ..serializers import RequestSerializer


class RequestListCreate(generics.ListCreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def post(self, request):
        # Validate input
        serializer = RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get input
        member_id = request.data['member']
        team_id = request.data['team']

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

        serializer.save()
        return Response(
            {'result': f"{member.member_name}'s request to team {team.team_name} added"}, status=status.HTTP_200_OK
        )


class RequestListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
    lookup_field = 'pk'
