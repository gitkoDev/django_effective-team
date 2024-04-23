from django.urls import path
from .views import (
    CreatorList,
    CreatorListRetrieveUpdateDestroy,
    TeamList,
    TeamListRetrieveUpdateDestroy,
    MemberList,
    MemberListRetrieveUpdateDestroy,
    RequestList,
    RequestListRetrieveUpdateDestroy,
    index,
)

urlpatterns = [
    path('', index),
    path('creators/', CreatorList.as_view()),
    path('creators/<int:pk>/', CreatorListRetrieveUpdateDestroy.as_view()),
    path('teams/', TeamList.as_view()),
    path('teams/<int:pk>/', TeamListRetrieveUpdateDestroy.as_view()),
    path('members/', MemberList.as_view()),
    path('members/<int:pk>/', MemberListRetrieveUpdateDestroy.as_view()),
    path('requests/', RequestList.as_view()),
    path('requests/<int:pk>/', RequestListRetrieveUpdateDestroy.as_view()),
]
