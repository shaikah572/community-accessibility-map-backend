from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields = ['id']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class MarkerSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    category_id =serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = Marker
        fields = '__all__'
        read_only_fields = ['created_by']



class CommentSerializer(serializers.ModelSerializer):

    marker = MarkerSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'