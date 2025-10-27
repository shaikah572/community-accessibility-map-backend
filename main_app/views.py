from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


# Create your views here.

class CategoryIndex(APIView):

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
