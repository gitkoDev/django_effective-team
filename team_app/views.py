from django.http import HttpResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.views import exception_handler
from rest_framework.response import Response


from .models import (
    Creator,
    Team,
    Member,
    Request,
    Transaction
)

from .serializers import (
    CreatorSerializer,
    TeamSerializer,
    MemberSerializer,
    RequestSerializer,
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
    
class RequestListCreate(generics.ListCreateAPIView):
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
    
# Transaction view
class TransactionListCreate(APIView):
    def get_request_data(self, request):
        try:
            amount = request.data['amount']
        except:
            return Response(
                {'result': 'Please provide valid amount to transfer'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            sender_id = request.data['sender']
            receiver_id = request.data['receiver']   
        except:
            return Response(
                {'result': 'Please provide valid sender and receiver id'},
                status=status.HTTP_400_BAD_REQUEST
            )   
        return amount, sender_id, receiver_id
    
    def validate_input(self, request, amount, sender_id, receiver_id):
        if (not sender_id or not receiver_id):
            return False, Response(
            {'result': 'Please provide valid and receiver id'},
            status=status.HTTP_400_BAD_REQUEST)
            
        if float(sender_id) <= 0 or float(receiver_id) <= 0:
            return False, Response(
            {'result': 'Please provide valid and receiver id'},
            status=status.HTTP_400_BAD_REQUEST) 
                           
        if sender_id == receiver_id:
            return False, Response(
            {'result': 'Sender and receiver should be different'},
            status=status.HTTP_400_BAD_REQUEST
            )
        
        if (not amount):
            return False, Response(
                {'result': 'Please provide valid amount to transfer'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        if amount <= 0:
            return False, Response(
                {'result': 'amount to transfer should be greater than zero'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return True, None
    
    def get_creators(self, sender_id, receiver_id):
        try:
            sender_id = Creator.objects.get(id=sender_id)
            receiver_id = Creator.objects.get(id=receiver_id)
            return sender_id, receiver_id
        except:
            return
        
    def serialize_creators(self, creator):
        data = {
           'creator_name': creator.creator_name,
            'money': creator.money
        }
        
        serializer = CreatorSerializer(instance = creator, data=data)
        if serializer.is_valid():
            serializer.save()
                
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
            {"result": "no transactions yet"},
            status=status.HTTP_400_BAD_REQUEST
        )


    def post(self, request):        
        # Get all request body fields
        try:
            amount, sender_id, receiver_id = self.get_request_data(request)
        except: 
            return self.get_request_data(request)
        
        # Validate input
        is_input_valid, response =  self.validate_input(request, amount, sender_id, receiver_id)
        if not is_input_valid:
            return response

        # Check if creators exist
        try:
            sender, receiver = self.get_creators(sender_id=sender_id, receiver_id=receiver_id)
        except:
            return Response(
                {'result': 'Please provide existing sender and receiver id, no creators found'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Validate transaction amount
        if sender.money - amount < 0:
            return Response(
                {"result: Creator doesn't have enough money to transfer"},
                status=status.HTTP_400_BAD_REQUEST
            )
          
        # Process transaction  
        sender.money -= amount
        receiver.money += amount
        
        # Serialize creators
        self.serialize_creators(sender)
        self.serialize_creators(receiver)
        
        # Serialize transaction
        data = {
            'sender': sender.id,
            'receiver': receiver.id,
            'amount': amount 
        }
        
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        return Response(
            {f'{serializer.data}'},
            status=status.HTTP_200_OK
        )
    
 
def index(request):
    return HttpResponse('index page')

