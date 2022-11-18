from django.shortcuts import render, redirect
from .models import Project, Slideshow, Comment, Gallery
from .forms import CommentForm
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

"""
def home(request):
    slideshow = Slideshow.objects.all()
    count = Slideshow.objects.all().count()
    context = {
        'slideshow': slideshow,
        'count': count,
                }
    return render(request, 'home/home.html', context)
"""


class Home(ListView):
    model = Slideshow
    template_name = 'home/home.html'
    context_object_name = 'slideshow'
    ordering = ['date']

def about(request):
    context = {
                }
    return render(request, 'home/about.html', context)

"""
def projects(request):
    context = {
        'project': Project.objects.all(),

    }
    return render(request, 'home/projects.html', context)
"""

class Projects(ListView):
    model = Project
    template_name = 'home/projects.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'project'
    ordering = ['-date']
    paginate_by = 5

def impacts(request):
    context = {
                }
    return render(request, 'home/impacts.html', context)

def gallery(request):
    context = {
        'photos': Gallery.objects.all()
                }
    return render(request, 'home/gallery.html', context)

def contact(request):
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            form = CommentForm()
        messages.success(request, f'Your Comment has been sent')
        return redirect('contact')
    context = {'form': form}
    return render(request, 'home/contact.html', context)

"""
def comments(request):
    comment = Comment.objects.all()
    context = {
        'comment': comment,
    }
    return render(request, 'home/comments.html', context)
"""

class CommentListView(ListView):
    model = Comment
    template_name = 'home/comments.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'comment'
    ordering = ['-posted']
    paginate_by = 10

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'home/project-detail.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'project'

"""
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    #<app>/<model>_<viewtype>.html

"""
