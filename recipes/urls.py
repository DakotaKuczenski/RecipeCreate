from django.urls import path, re_path, include
from django.conf.urls import url
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, search_post, favorite_post, recipesfavorites
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', PostListView.as_view(), name='recipe-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='recipe-about'),
    path('blog/', views.blog, name='recipe-blog'),
    re_path(r'^results/$', search_post, name='search_post'),
    path('post/<int:pk>/favorite_post/', favorite_post, name="favorite_post"),
    path('post/recipesfavorites/', recipesfavorites, name="recipesfavorites"),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
