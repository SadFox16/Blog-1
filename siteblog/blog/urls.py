from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home_page'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetSinglePost.as_view(), name='post'),
]
