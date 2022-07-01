from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home_page'),
    path('category/<str:slug>', get_category, name='category'),
]
