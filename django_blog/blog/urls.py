from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # Blog posts CRUD
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  # list all posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # create post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # post details
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # edit post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # delete post
]
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns += [
    path('posts/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
