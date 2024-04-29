from django.db import models

# Create your models here.


class Creator(models.Model):
    creator_name = models.CharField(max_length=250)
    money = models.FloatField(default=0)

    def __str__(self):
        # return f'{self.id}'
        return self.creator_name


class Team(models.Model):
    team_size = models.IntegerField(default=1)
    team_name = models.CharField(max_length=250)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name


class Member(models.Model):
    member_name = models.CharField(max_length=250)
    stamina = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.member_name


class Request(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.member_name}'s request to {self.team.team_name}"


class Transaction(models.Model):
    sender = models.ForeignKey(
        Creator, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        Creator, on_delete=models.CASCADE, related_name='receiver')
    amount = models.FloatField(default=0)

    def __str__(self):
        return f'From: {self.sender.creator_name} to {self.receiver.creator_name}. Amount: {self.amount}'
