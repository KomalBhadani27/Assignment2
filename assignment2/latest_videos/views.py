from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import LatestVideoSerializer
from .models import LatestVideos


class LatestVideosViewSet(viewsets.ModelViewSet):
    queryset = LatestVideos.objects.all()
    serializer_class = LatestVideoSerializer
