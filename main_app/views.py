from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, 
    IsAuthenticated, 
    IsAdminUser,
    AllowAny )

from .models import *
from .serializers import *

from django.shortcuts import get_object_or_404

# Create your views here.

# ------ Category requests
class CategoryIndex(APIView):

    def get(self, request):
        try:
            queryset = Category.objects.all()
            serializer = CategorySerializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CategoryDetail(APIView):

    def get(self, request, category_id):
        try: 
            queryset = get_object_or_404(Category, id=category_id)
            serializers = CategorySerializer(queryset)

            return Response(serializers.data, status=status.HTTP_200_OK)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self,request, category_id):
        try:
            queryset = get_object_or_404(Category, id=category_id)
            serializer = CategorySerializer(queryset, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def delete(self,request, category_id):
        try:
            queryset = get_object_or_404(Category, id=category_id)
            queryset.delete()

            return Response(
                {'message': f'Category {category_id} has been deleted.'},
                status=status.HTTP_204_NO_CONTENT)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# ----------


# ------ Marker requests
class MarkerIndex(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        try:
          queryset = Marker.objects.all()
          serializer = MarkerSerializer(queryset, many=True)

          return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            serializer = MarkerSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(created_by = request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

       
class MarkerDetail(APIView):
    # stackoverflow > "How to set different permission_classes for GET and POST requests using the same URL?"
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get(self, request, marker_id):
        try:
            queryset = get_object_or_404(Marker, id=marker_id)
            serializer = MarkerSerializer(queryset)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, marker_id):
        try:
            queryset = get_object_or_404(Marker, id=marker_id)
            serializer = MarkerSerializer(queryset, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, marker_id):
        try:
            queryset = get_object_or_404(Marker, id=marker_id)
            queryset.delete()

            return Response(
                {'message': f'Marker {marker_id} has been deleted.'},
                status=status.HTTP_204_NO_CONTENT)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# ----------


# ------ Comment requests
class CommentIndex(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, marker_id):
        try:
            queryset = Comment.objects.filter(marker=marker_id)
            serializer = CommentSerializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request, marker_id):
        try:
            serializer = CommentSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(created_by = request.user, marker_id=marker_id)
                queryset = Comment.objects.filter(marker=marker_id)
                serializer = CommentSerializer(queryset, many=True)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CommentDelete(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, marker_id, comment_id):
        try:
            queryset = get_object_or_404(Comment, id=comment_id, marker=marker_id)
            queryset.delete()

            return Response(
                {'message': f'comment {comment_id} has been deleted'},
                status=status.HTTP_204_NO_CONTENT)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# ----------







        
    

        
          
        