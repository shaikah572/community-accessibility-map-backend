from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserDetail.as_view(), name='user_detail'),
    path('user/delete/', UserDelete.as_view(), name='user_delete'),
    path('markers/', MarkerIndex.as_view(), name='marker_index'),
    path('markers/<int:marker_id>/', MarkerDetail.as_view(), name='marker_detail'),
    path('markers/<int:marker_id>/comments/', CommentIndex.as_view(), name='comment_index'),
    path('markers/<int:marker_id>/comments/<int:comment_id>/', CommentDelete.as_view(), name='comment_delete'),
    path('categories/', CategoryIndex.as_view(), name='category_index'),
    path('categories/<int:category_id>/', CategoryDetail.as_view(), name='category_detail'),
]