from django.urls import path
from .views import *

urlpatterns = [
    path('markers/', MarkerIndex.as_view(), name='marker_index'),
    path('markers/<int:marker_id>/', MarkerDetail.as_view(), name='marker_detail'),
    path('markers/<int:marker_id>/comments/', CommentIndex.as_view(), name='comment_index'),
    path('markers/<int:marker_id>/comments/<int:comment_id>/', CommentDelete.as_view(), name='comment_delete'),
    path('categories/', CategoryIndex.as_view(), name='category_index'),
    path('categories/<int:category_id>/', CategoryDetail.as_view(), name='category_detail'),
]