from django.shortcuts import render
from rest_framework import status, viewsets
from .models import Image
from .serializer import ImageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

# Need to test with image list