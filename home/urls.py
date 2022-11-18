from django.urls import path
from . import views
from .views import CommentListView, Projects, ProjectDetailView, Home



urlpatterns = [
    #path('', views.home, name='blog-home'), this used the fuction view
    path('', Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('projects/', Projects.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('impacts/', views.impacts, name='impacts'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    #path('comments/', views.comments, name='comments'),
    path('comments/', CommentListView.as_view(), name='comments'),
    
]






"""
urlpatterns = [
    #path('', views.home, name='blog-home'), this used the fuction view
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]

#<app>/<model>_<viewtype>.html
"""
