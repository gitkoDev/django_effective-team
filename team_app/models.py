from django.db import models

# Create your models here.
class Creator(models.Model):
    name = models.CharField(max_length=250)
    money = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.name
    
class Team(models.Model):
    team_name = models.CharField(max_length=250)
    team_creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.team_name
    
class Member(models.Model):
    name = models.CharField(max_length=250)
    stamina = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Request(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.member.name}'s request to {self.team.team_name}"


