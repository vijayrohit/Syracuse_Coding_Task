from django.urls import path

from .views import (
    MusicListView,
    MusicDetailView,
    MusicCreateView,
    MusicUpdateView,
    MusicDeleteView
)
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='library-home'),
    path('post/<int:pk>/', MusicDetailView.as_view(), name='music-detail'),
    path('post/new/', MusicCreateView.as_view(), name='music-create'),
    path('post/<int:pk>/update/', MusicUpdateView.as_view(), name='music-update'),
    path('post/<int:pk>/delete/', MusicDeleteView.as_view(), name='music-delete'),
    path('about/', views.about, name='library-about'),
    path('songcount/', views.titleCount, name='admin-count')
]