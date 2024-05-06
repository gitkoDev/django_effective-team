from rest_framework import serializers

from ..models import Request, Member, Team


class RequestPostSerializer(serializers.ModelSerializer):
    member = serializers.IntegerField(source='member.id')
    team = serializers.IntegerField(source='team.id')

    class Meta:
        model = Request
        fields = ['member', 'team']

    def validate(self, data):
        member_id = data['member']['id']
        team_id = data['team']['id']

        try:
            member = Member.objects.get(id=member_id)
        except:
            raise serializers.ValidationError("member doesn't exist")

        try:
            team = Team.objects.get(id=team_id)
        except:
            raise serializers.ValidationError("team doesn't exist")

        # Check to make sure request for the same member and team doesn't exist already
        request = Request.objects.filter(member=member, team=team)
        if request:
            raise serializers.ValidationError(
                f"{member.member_name}'s request to team {team.team_name} already exists")

        # Check to make sure member isn't already in the team
        for memb in team.members.values_list():
            if memb[0] == int(member_id):
                raise serializers.ValidationError(
                    f"{member.member_name} is already in team {team.team_name}")

        return data

    def create(self, validated_data):
        member_id = validated_data['member']['id']
        member = Member.objects.get(id=member_id)

        team_id = validated_data['team']['id']
        team = Team.objects.get(id=team_id)

        return Request.objects.create(member=member, team=team)


class RequestGetSerializer(serializers.ModelSerializer):
    member = serializers.IntegerField(source='member.id')

    class Meta:
        model = Request
        fields = ['member']
