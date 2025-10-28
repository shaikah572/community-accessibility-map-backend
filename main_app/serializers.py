from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class MarkerSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(read_only=True, source='category.name')

    class Meta:
        model = Marker
        fields = '__all__'
        read_only_fields = ['created_by']



class CommentSerializer(serializers.ModelSerializer):

    marker_name = serializers.CharField(read_only=True, source='marker.name')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_by', 'marker']