from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Transaction
from ..serializers import TransactionSerializer


class TransactionListCreate(APIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        if queryset:
            serializer = TransactionSerializer(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            {"error": "no transactions yet"},
            status=status.HTTP_400_BAD_REQUEST
        )

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
