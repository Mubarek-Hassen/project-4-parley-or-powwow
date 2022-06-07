from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('posts/', views.Posts.as_view(), name = "posts"),
    path('posts/new/', views.New.as_view(), name = "new"),
    path('posts/<int:pk>/', views.BlogDetail.as_view(), name="blog_detail"),
    path('posts/<int:pk>/update', views.BlogUpdate.as_view(), name="blog_update"),
    path('posts/<int:pk>/delete', views.BlogDelete.as_view(), name="blog_delete"),
    
]