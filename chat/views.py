from django.shortcuts import render
# Imports room model
from .models import Room, Comment
# Import ListView for ClassBased view of posts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Import LoginRequierd for post views exclusive for logged in users
from django.contrib.auth.mixins import LoginRequiredMixin
# Imports PassesTest for post edit exclusive for authors
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
def home(request):
    return render(request, 'chat/home.html')

# Shows all posts, can be used as user's homepage
class RoomListView(ListView):
    model = Room
    template_name = 'chat/home.html'
    context_object_name = 'rooms'
    ordering = ['-id']

class RoomDetailView(DetailView):
    model = Room

class RoomCreateView(CreateView):
    model = Room
    fields = ['name']
    
# Abstract comment instance
class CommentCreateView(CreateView):
    model = Comment
    # User only inputs reaction id, must be tuple
    fields = ['name', 'comment']
    # Redirects to self
    success_url = '#'
    # Performs valid_form check before POST
    def form_valid(self, form):
        # Sets the current post attribute for the instance as
        # the fk given in the URL
        form.instance.post = Room.objects.get(pk=self.kwargs['fk'])
        # super() back with a valid instance
        return super().form_valid(form)

    # Get comments for this Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments']= Comment.objects.all().filter(post=self.kwargs['fk']).order_by('-id')[:3]
        context['room'] = Room.objects.get(pk=self.kwargs['fk'])
        return context