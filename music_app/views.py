from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Song, User
from django.db.models import Count
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

# User Detail Page
class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        context['songs'] = user.songs.all()
        return context

# For future search functionality
def song_search(request):
    query = request.GET.get('query')
    songs = Song.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'songs': songs})


# Additional functions or class-based views for login, logout, user management, etc. can be added accordingly.
