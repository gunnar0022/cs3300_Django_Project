from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Count

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .models import Song
from .forms import SongDeleteForm
from .forms import SongAddForm
from .forms import SongEditForm
from .models import UserProfile

from django.urls import reverse_lazy
from django.urls import reverse


# Base_template/index.html
class HomeListView(ListView):
    model = Song
    template_name = 'index.html'
    context_object_name = 'songs'

    def get_queryset(self):
        return Song.objects.annotate(user_count=Count('users')).order_by('-user_count')[:10]

# Song List Page
class SongListView(ListView):
    model = Song
    template_name = 'song_list.html'
    context_object_name = 'songs'

# For adding a new song. This assumes you'll have a form for Song.
class SongCreateView(LoginRequiredMixin, CreateView):
    model = Song
    template_name = 'song_form.html'
    fields = ['name', 'instrument', 'genre']

# Song Detail Page
class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'
    context_object_name = 'song'

# For editing a song.
class SongUpdateView(LoginRequiredMixin, UpdateView):
    model = Song
    template_name = 'song_form.html'
    fields = ['name', 'instrument', 'genre']

# For deleting a song.
class SongDeleteView(LoginRequiredMixin, DeleteView):
    model = Song
    template_name = 'song_confirm_delete.html'
    success_url = reverse_lazy('song_list')

# UserProfile Detail Page
class UserDetailView(DetailView):
    model = UserProfile
    template_name = 'user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        context['songs'] = user.songs.all()
        return context

# For future search functionality
def song_search(request):
    query = request.GET.get('query')
    songs = Song.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'songs': songs})



def add_song(request):
    if request.method == 'POST':
        form = SongAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongAddForm()
    return render(request, 'add_song.html', {'form': form})

def edit_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        form = SongEditForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_detail', song_id=song.id)
    else:
        form = SongEditForm(instance=song)
    return render(request, 'edit_song.html', {'form': form})



def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        form = SongDeleteForm(request.POST, instance=song)
        if form.is_valid():
            song.delete()
            return redirect('song_list')
    else:
        form = SongDeleteForm(instance=song)
    return render(request, 'delete_song.html', {'form': form, 'song': song})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'song_detail.html', {'song': song})


# Login view
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page or wherever you want
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Registration view
def register_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to home page or wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



class UserDetailView(DetailView):
    model = UserProfile
    template_name = 'user_detail.html'
    context_object_name = 'userprofile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['learned_songs'] = self.object.learned_songs.all()
        context['liked_songs'] = self.object.liked_songs.all()
        return context
    

@login_required
def add_to_liked_songs(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    user_profile = request.user.userprofile
    user_profile.liked_songs.add(song)

    if song not in user_profile.liked_songs.all():
        user_profile.liked_songs.add(song)
        messages.success(request, 'Song added to your Want to Learn list!')
    else:
        messages.info(request, 'Song is already in your Want to Learn list!')

    return redirect('song_detail', pk=song_id)