from django.urls import path
from .views import HomeView, AddPost, UpdatePost, DeletePost,CategoryView,DetailView,LikeView


urlpatterns = [
    path('', HomeView, name='home'),
    path('post/<int:pk>', DetailView, name='detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('post/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    path('category/<str:cat>/', CategoryView, name='category'),
    path('like/<int:pk>',LikeView,name='like_post'),
]
