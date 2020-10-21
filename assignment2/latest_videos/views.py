from django.shortcuts import redirect

# Create your views here.

from rest_framework import viewsets, generics, filters
from django.contrib.postgres.search import TrigramSimilarity

from .serializers import LatestVideoSerializer
from .models import LatestVideos, VideoByCategory


class LatestVideosViewSet(viewsets.ModelViewSet):

    queryset = LatestVideos.objects.all().order_by('-published_at')
    serializer_class = LatestVideoSerializer


class SearchVideosViewSet(generics.ListCreateAPIView):
    """Implements fuzzy search on the title and description of the latest videos"""
    serializer_class = LatestVideoSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            query = self.request.GET.get('query', None)
            if query:
                return LatestVideos.objects.annotate(
                                similarity=TrigramSimilarity('desc', str(query)),
                            ).filter(similarity__gt=0.05).order_by('-similarity')\
                    .order_by('-published_at')
            else:
                return LatestVideos.objects.all().order_by('-published_at')
