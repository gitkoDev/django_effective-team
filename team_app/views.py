from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import (
    Creator,
    Team,
    Member,
    Request
)

# List views
class CreatorList(ListView):
    model = Creator
    context_object_name = 'creators'
    template_name = 'creators_list.html'
    
class TeamList(ListView):
    model = Team
    context_object_name = 'teams'
    template_name = 'teams_list.html'    

class MemberList(ListView):
    model = Member
    context_object_name = 'members'
    template_name = 'members_list.html'
     
class RequestList(ListView):
    model = Request
    context_object_name = 'requests'
    template_name = 'requests_list.html'
    


def index(request):
    return HttpResponse('index page')



# creator
# team
# member
# request