from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryIndex.as_view(), name='category_index'),
]