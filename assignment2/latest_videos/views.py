from django.shortcuts import redirect

# Create your views here.

from rest_framework import viewsets, generics

from .serializers import LatestVideoSerializer, SearchAPISerializer
from .models import LatestVideos, VideoByCategory


class LatestVideosViewSet(viewsets.ModelViewSet):
    queryset = LatestVideos.objects.all().order_by('-published_at')
    serializer_class = LatestVideoSerializer


class SearchVideosViewSet(generics.ListCreateAPIView):
    serializer_class = SearchAPISerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            query = self.request.GET.get('query', None)
            if query:
                return LatestVideos.objects.filter(category__type_id=query).order_by('-published_at')
            else:
                return LatestVideos.objects.all().order_by('-published_at')
