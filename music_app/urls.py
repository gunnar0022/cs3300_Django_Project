from django.urls import path
from . import views

from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, World!")

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.HomeListView.as_view(), name='home'),
path('songs/', views.SongListView.as_view(), name='song_list'),
path('songs/add/', views.SongCreateView.as_view(), name='song_add'),
path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song_detail'),
path('songs/<int:pk>/edit/', views.SongUpdateView.as_view(), name='song_edit'),
path('songs/<int:pk>/delete/', views.SongDeleteView.as_view(), name='song_delete'),
path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
path('search/', views.song_search, name='song_search'),
]
