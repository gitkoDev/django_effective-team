from django.urls import path

from .views import (
    CreatorListCreate,
    CreatorListRetrieveUpdateDestroy,
    MemberListCreate,
    MemberListRetrieveUpdateDestroy,
    TeamRequestListCreate,
    TeamListCreate,
    TeamListRetrieveUpdateDestroy,
    TeamRecruitListCreate,
    TransactionListCreate,
)

urlpatterns = [
    path('creators/', CreatorListCreate.as_view()),
    path('creators/<int:pk>/', CreatorListRetrieveUpdateDestroy.as_view()),
    path('teams/', TeamListCreate.as_view()),
    path('teams/<int:pk>/', TeamListRetrieveUpdateDestroy.as_view()),
    path('teams/<int:pk>/request/', TeamRequestListCreate.as_view()),
    path('teams/<int:pk>/recruit/', TeamRecruitListCreate.as_view()),
    path('members/', MemberListCreate.as_view()),
    path('members/<int:pk>/', MemberListRetrieveUpdateDestroy.as_view()),
    path('transactions/', TransactionListCreate.as_view()),
]
