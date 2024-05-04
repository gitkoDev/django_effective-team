from django.db import transaction

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from ..models import Transaction, Creator
from ..serializers import TransactionSerializer


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
        sender = Creator.objects.get(id=sender_id)
        receiver = Creator.objects.get(id=receiver_id)

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
            data=serializer.data,
            status=status.HTTP_200_OK
        )
