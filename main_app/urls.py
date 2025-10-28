from django.urls import path
from .views import *

urlpatterns = [
    path('markers/', MarkerIndex.as_view(), name='marker_index'),
    path('markers/<int:marker_id>/', MarkerDetail.as_view(), name='marker_detail'),
    path('categories/', CategoryIndex.as_view(), name='category_index'),
    path('categories/<int:category_id>/', CategoryDetail.as_view(), name='category_detail'),
]