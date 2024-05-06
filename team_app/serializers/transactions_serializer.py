from django.db import transaction
from rest_framework import serializers

from ..models import Transaction, Creator


class TransactionSerializer(serializers.ModelSerializer):
    sender = serializers.IntegerField(source='sender.id')
    receiver = serializers.IntegerField(source='receiver.id')

    class Meta:
        model = Transaction
        fields = ['sender', 'receiver', 'amount']

    def validate(self, data):
        sender_id = data['sender']['id']
        receiver_id = data['receiver']['id']
        amount = data['amount']

        try:
            sender = Creator.objects.get(id=sender_id)
        except:
            raise serializers.ValidationError("sender doesn't exist")

        try:
            Creator.objects.get(id=receiver_id)
        except:
            raise serializers.ValidationError("receiver doesn't exist")

        if not amount or amount <= 0:
            raise serializers.ValidationError("invalid amount")

        if sender.money - amount < 0:
            raise serializers.ValidationError(
                "sender doesn\'t have enough money")

        return data

    def create(self, validated_data):
        sender_id = validated_data['sender']['id']
        sender = Creator.objects.get(id=sender_id)

        receiver_id = validated_data['receiver']['id']
        receiver = Creator.objects.get(id=receiver_id)

        amount = validated_data['amount']

        with transaction.atomic():
            sender.money -= amount
            receiver.money += amount
            sender.save()
            receiver.save()

        return Transaction.objects.create(sender=sender, receiver=receiver, amount=amount)
