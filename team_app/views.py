from django.db import transaction
from django.http import HttpResponse

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Creator, Member, Request, Team, Transaction

from .serializers import (
    CreatorSerializer,
    MemberSerializer,
    RequestSerializer,
    TeamSerializer,
    TransactionSerializer
)


# List views
# class CreatorListCreate(generics.ListCreateAPIView):
#     serializer_class = CreatorSerializer
#     queryset = Creator.objects.all()


# class TeamListCreate(generics.ListCreateAPIView):
#     serializer_class = TeamSerializer
#     queryset = Team.objects.all()


# class MemberListCreate(generics.ListCreateAPIView):
#     serializer_class = MemberSerializer
#     queryset = Member.objects.all()

#     def get(self, request):
#         members = Member.objects.all().order_by('stamina')
#         serializer = MemberSerializer(members, many=True)
#         return Response(
#             serializer.data, status=status.HTTP_200_OK
#         )


# class RequestListCreate(generics.ListCreateAPIView):
#     serializer_class = RequestSerializer
#     queryset = Request.objects.all()

#     def post(self, request):
#         # Validate input
#         serializer = RequestSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         # Get input
#         member_id = request.data['member']
#         team_id = request.data['team']

#         # Get member and team objects
#         member = Member.objects.get(id=member_id)
#         team = Team.objects.get(id=team_id)

#         # Check to make sure request for the same member and team doesn't exist already
#         request = Request.objects.filter(member=member, team=team)
#         if request:
#             return Response(
#                 {'error:': f"{member.member_name}'s request to team {team.team_name} already exists"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         # Check to make sure member isn't already in the team
#         for memb in team.members.values_list():
#             if memb[0] == member_id:
#                 return Response(
#                 {'error:': f"{member.member_name} is already in team {team.team_name}"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         serializer.save()
#         return Response(
#             {'result': f"{member.member_name}'s request to team {team.team_name} added"}, status=status.HTTP_200_OK
#         )


# Detail views
# class CreatorListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CreatorSerializer
#     queryset = Creator.objects.all()
#     lookup_field = 'pk'


# class TeamListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TeamSerializer
#     queryset = Team.objects.all()
#     lookup_field = 'pk'


# class MemberListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = MemberSerializer
#     queryset = Member.objects.all()
#     lookup_field = 'pk'


# class RequestListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = RequestSerializer
#     queryset = Request.objects.all()
#     lookup_field = 'pk'


# Transaction view
# class TransactionListCreate(APIView):
#     serializer_class = TransactionSerializer

#     def get(self, request):
#         try:
#             transactions = Transaction.objects.all()
#             serializer = TransactionSerializer(transactions, many=True)
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_200_OK
#             )
#         except:
#             return Response(
#                 {"error": "no transactions yet"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#     def post(self, request):
#         # Validate input
#         serializer = TransactionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         # Get input
#         sender_id = request.data['sender']
#         receiver_id = request.data['receiver']
#         amount = float(request.data['amount'])

#         # Get creators
#         sender = Creator.objects.get(id=sender_id)
#         receiver = Creator.objects.get(id=receiver_id)

#         # Process transaction
#         if sender.money - amount < 0:
#             return Response(
#                 {'error': 'sender doesn\'t have enough money'}, status=status.HTTP_400_BAD_REQUEST
#             )
#         else:
#             with transaction.atomic():
#                 sender.money -= amount
#                 receiver.money += amount
#                 sender.save()
#                 receiver.save()

#         serializer.save()

#         return Response(
#             data=serializer.data,
#             status=status.HTTP_200_OK
#         )


# Team recruitement view (sorting requests)
# class TeamRecruitCreate(generics.CreateAPIView):
#     lookup_field = 'pk'

#     def post(self, request, pk):
#         # Check if team with this pk exists
#         try:
#             team = Team.objects.get(id=pk)
#         except:
#             return Response({'error': "team doesn't exist"})

#         # Get all requests to the team
#         requests = Request.objects.filter(team=pk)

#         if not requests:
#             return Response({'error': f'no requests to {team.team_name}'}, status=status.HTTP_400_BAD_REQUEST)

#         # Process recruitment
#         team_limit = team.team_size
#         current_team_size = len(team.members.values_list())
#         spots_left = team_limit - current_team_size
#         members_added = 0

#         # If team limit is exceeded, don't add anyone
#         if current_team_size >= team_limit:
#             return Response({'error': f'{team.team_name} has no more space in the team'}, status=status.HTTP_400_BAD_REQUEST)

#         # If not enough space in team for all new members, sort them by stamina
#         if current_team_size + len(requests) > team_limit:
#             with transaction.atomic():
#                 for i in range(0, spots_left):
#                     team.members.add(requests[i].member)
#                     members_added += 1
#                     requests[i].delete()
#                 team.save()

#             return Response({'result': f'{members_added} new members added to team {team.team_name}. Some new members not added'}, status=status.HTTP_200_OK)

#         # If enough space for everyone, add them
#         with transaction.atomic():
#             for request in requests:
#                 team.members.add(request.member)
#                 members_added += 1
#             requests.delete()
#             team.save()

#         return Response({'result': f'{members_added} new members added to team {team.team_name}'}, status=status.HTTP_200_OK)


def index(request):
    return HttpResponse('index page')
