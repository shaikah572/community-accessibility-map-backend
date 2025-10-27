from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryIndex.as_view(), name='category_index'),
    path('categories/<int:category_id>/', CategoryDetail.as_view(), name='category_detail'),
]