from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response
from ..models import Team, Request
from ..serializers import RequestPostSerializer


class TeamRecruitListCreate(generics.CreateAPIView):
    serializer_class = RequestPostSerializer
    lookup_field = 'pk'

    def sort_by_stamina(self, requests):
        sorted = []
        for request in requests:
            sorted.append(request)

        for i in range(0, len(sorted) - 1):
            for j in range(i + 1, len(sorted)):
                if sorted[j].member.stamina > sorted[i].member.stamina:
                    sorted[i], sorted[j] = sorted[j], sorted[i]

        return sorted

    def post(self, request, pk):
        # Check if team with this pk exists
        try:
            team = Team.objects.get(id=pk)
        except:
            return Response({'error': "team doesn't exist"})

        # Get all requests to the team
        requests = Request.objects.filter(team=pk)
        if not requests:
            return Response({'error': f'no requests to {team.team_name}'}, status=status.HTTP_400_BAD_REQUEST)

        # Process recruitment
        team_limit = team.team_size
        current_team_size = len(team.members.values_list())
        spots_left = team_limit - current_team_size
        members_added = 0

        # If team limit is exceeded, don't add anyone
        if current_team_size >= team_limit:
            return Response({'error': f'{team.team_name} has no more space in the team'}, status=status.HTTP_400_BAD_REQUEST)

        # If not enough space in team for all new members, sort them by stamina and add best ones
        if current_team_size + len(requests) > team_limit:
            sorted_requests = self.sort_by_stamina(requests)

            with transaction.atomic():
                for i in range(0, spots_left):
                    team.members.add(sorted_requests[i].member)
                    members_added += 1
                    requests[i].delete()
                team.save()

            return Response({'result': f'{members_added} new members added to team {team.team_name}. Some new members not added'}, status=status.HTTP_200_OK)

        # If enough space for everyone, add them
        with transaction.atomic():
            for request in requests:
                team.members.add(request.member)
                members_added += 1
            requests.delete()
            team.save()

        return Response({'result': f'{members_added} new members added to team {team.team_name}'}, status=status.HTTP_200_OK)
