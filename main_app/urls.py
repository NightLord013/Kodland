from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post/new_post/', views.new_post, name = 'new_post'),
]
