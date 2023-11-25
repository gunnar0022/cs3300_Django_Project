from django.http import HttpResponse
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import login_request, register_request, UserDetailView, add_to_liked_songs, rate_song

def my_view(request):
    return HttpResponse("Hello, World!")

urlpatterns = [
path('', views.HomeListView.as_view(), name='home'),
path('songs/', views.SongListView.as_view(), name='song_list'),
path('songs/add/', views.SongCreateView.as_view(), name='song_add'),
path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song_detail'),
path('songs/<int:pk>/edit/', views.SongUpdateView.as_view(), name='song_edit'),
path('songs/<int:pk>/delete/', views.SongDeleteView.as_view(), name='song_delete'),
path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
path('search/', views.song_search, name='song_search'),
path('songs/', views.song_list, name='song_list'),  # This 'name' is used for the redirect
path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
path('song/add/', views.add_song, name='song_add'),
path('song/<int:song_id>/edit/', views.edit_song, name='song_edit'),
path('song/<int:song_id>/delete/', views.delete_song, name='song_delete'),
path('login/', login_request, name='login'),
path('register/', register_request, name='register'),
path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
path('user/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
path('songs/<int:song_id>/liked_songs/', add_to_liked_songs, name='add_to_liked_songs'),
path('rate_song/<int:song_id>/', rate_song, name='rate_song'),



]
