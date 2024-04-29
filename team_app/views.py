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
class CreatorListCreate(generics.ListCreateAPIView):
    serializer_class = CreatorSerializer
    queryset = Creator.objects.all()


class TeamListCreate(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class MemberListCreate(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    def get(self, request):
        members = Member.objects.all().order_by('stamina')
        serializer = MemberSerializer(members, many=True)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )


class RequestListCreate(generics.ListCreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def post(self, request):

        return Response(
            {'result': 'aaa'}, status=status.HTTP_200_OK
        )


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


# Transaction view
class TransactionListCreate(APIView):
    serializer_class = TransactionSerializer

    def get(self, request):
        try:
            transactions = Transaction.objects.all()
            serializer = TransactionSerializer(transactions, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {"error": "no transactions yet"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        # Validate input
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get input
        sender_id = request.data['sender']
        receiver_id = request.data['receiver']
        amount = float(request.data['amount'])

        # Get creators
        try:
            sender = Creator.objects.get(id=sender_id)
            receiver = Creator.objects.get(id=receiver_id)
        except:
            return Response(
                {'error': 'Please provide existing sender and receiver id'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Process transaction
        if sender.money - amount < 0:
            return Response(
                {'error': 'sender doesn\'t have enough money'}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            with transaction.atomic():
                sender.money -= amount
                receiver.money += amount
                sender.save()
                receiver.save()

        serializer.save()

        return Response(
            {f'{serializer.data}'},
            status=status.HTTP_200_OK
        )


def index(request):
    return HttpResponse('index page')
