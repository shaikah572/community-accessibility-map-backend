from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
                {'message': f'Category {category_id} has been delete.'},
                status=status.HTTP_204_NO_CONTENT)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# ----------


# ------ Marker requests
class MarkerIndex(APIView):

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
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

          
        