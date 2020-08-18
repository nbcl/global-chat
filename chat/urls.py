# Uses Django Paths
from django.urls import path
# Imports views.py
from . import views
from .views import RoomListView, RoomDetailView, RoomCreateView, CommentCreateView

# Sets all url patterns
urlpatterns = [
    path('', views.RoomListView.as_view(), name = "landing"),
    path('room/details/<int:pk>/', views.RoomDetailView.as_view(), name = "room-detail"),
    path('room/create/', views.RoomCreateView.as_view(), name = "room-create"),
    path('room/<int:fk>/', views.CommentCreateView.as_view(), name = "room-view"),
]