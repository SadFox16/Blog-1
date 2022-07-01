from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home_page'),
    path('category/<str:slug>/', get_category, name='category'),
    path('post/<str:slug>/', get_post, name='post'),
]
