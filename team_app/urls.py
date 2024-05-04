from django.urls import path

from . import views

from .views import (
    CreatorListCreate,
    CreatorListRetrieveUpdateDestroy,
    MemberListCreate,
    MemberListRetrieveUpdateDestroy,
    RequestListCreate,
    RequestListRetrieveUpdateDestroy,
    TeamListCreate,
    TeamListRetrieveUpdateDestroy,
    TeamRecruitCreate,
    TransactionListCreate,
    # index
)

urlpatterns = [
    # path('', index),
    path('creators/', CreatorListCreate.as_view()),
    path('creators/<int:pk>/', CreatorListRetrieveUpdateDestroy.as_view()),
    path('teams/', TeamListCreate.as_view()),
    path('teams/<int:pk>/', TeamListRetrieveUpdateDestroy.as_view()),
    path('teams/recruit/<int:pk>', TeamRecruitCreate.as_view()),
    path('members/', MemberListCreate.as_view()),
    path('members/<int:pk>/', MemberListRetrieveUpdateDestroy.as_view()),
    path('requests/', RequestListCreate.as_view()),
    path('requests/<int:pk>/', RequestListRetrieveUpdateDestroy.as_view()),
    path('transactions/', TransactionListCreate.as_view())
]
