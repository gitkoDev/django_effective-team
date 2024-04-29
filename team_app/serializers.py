from rest_framework import serializers

from .models import Creator, Member, Request, Team, Transaction


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ('__all__')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('__all__')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('__all__')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('__all__')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('__all__')

    def validate(self, data):
        if data['sender'] == data['receiver']:
            raise serializers.ValidationError(
                'sender and receiver can\'t be the same')
        elif data['amount'] <= 0:
            raise serializers.ValidationError(
                'amount has to be greater than 0')
        return data
