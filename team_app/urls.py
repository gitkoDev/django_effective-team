from django.urls import path
from .views import (
    CreatorList,
    TeamList,
    MemberList,
    RequestList,
    index,
)

urlpatterns = [
    path("", index),
    path("creators", CreatorList.as_view()),
    path("teams", TeamList.as_view()),
    path("members", MemberList.as_view()),
    path("requests", RequestList.as_view()),
]
