from django.urls import path
from . import views
from .models import Post

# urlpatterns = [
#   path('', views.list, name='blog'),
#   path('<int:id>/', views.post, name='post'),
# ]

# urlpatterns = [
#   path('', views.PostListView.as_view(), name='blog'),
#   path('<int:pk>/', views.PostDetailView.as_view(), name='post'),
# ]

from django.views.generic import ListView, DetailView

urlpatterns = [
   path('', ListView.as_view(
      queryset = Post.objects.all().order_by('-date'),
      template_name = 'blog/blog.html',
      context_object_name = 'Posts',
      paginate_by = 10)
      , name='blog'),
   path('<int:pk>/', views.post, name='post'),
]