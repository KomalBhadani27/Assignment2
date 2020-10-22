from django.shortcuts import redirect, HttpResponse

# Create your views here.

from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.contrib.postgres.search import TrigramSimilarity

from .serializers import LatestVideoSerializer
from .models import LatestVideos, VideoByCategory

DEFAULT_FIRST_PAGE = 1
DEFAULT_PER_PAGE = 5


class LatestVideosViewSet(viewsets.ModelViewSet):
    queryset = LatestVideos.objects.all().order_by('-published_at')
    serializer_class = LatestVideoSerializer


class SearchVideosViewSet(generics.ListCreateAPIView):
    """Implements fuzzy search on the title and description of the latest videos"""
    serializer_class = LatestVideoSerializer
    page = None
    per_page = None
    #Default query
    query = 'party'

    def get_queryset(self):
        """Overriding get_queryset method from parent class"""

        if self.request.method == 'GET':
            query = self.request.GET.get('query', None)
            self.page = self.request.GET.get('page', None)
            self.per_page = self.request.GET.get('per_page', None)

            if not self.page:
                self.page = DEFAULT_FIRST_PAGE
            else:
                self.page = int(self.page)

            if not self.per_page:
                self.per_page = DEFAULT_PER_PAGE
            else:
                self.per_page = int(self.per_page)

            offset = (self.page - 1) * self.per_page

            if query:
                self.query = query
                queryset = LatestVideos.objects.annotate(
                    similarity=TrigramSimilarity('desc', str(query)),
                ).filter(similarity__gt=0.05).order_by('-similarity') \
                               .order_by('-published_at')[offset: offset + self.per_page]
                return queryset
            else:
                return LatestVideos.objects.all().order_by('-published_at')

    def retrieve(self, request, *args, **kwargs):
        """Overriding retrieve method from parent class"""

        queryset = self.get_queryset()
        next_link, prev_link = self.__get_links()
        return Response({'next_link': next_link,
                         'prev_link': prev_link,
                         'latest_videos': LatestVideoSerializer(queryset, many=True).data})

    def list(self, request, *args, **kwargs):
        """Overriding list method from parent class"""

        queryset = self.get_queryset()
        next_link, prev_link = self.__get_links()
        return Response({'next_link': next_link,
                         'prev_link': prev_link,
                         'latest_videos': LatestVideoSerializer(queryset, many=True).data})

    def __get_links(self):
        # Helper links for pagination at frontend.
        next_link = '/videos?query=' + str(self.query) + 'page=' + str(self.page + 1) + '&per_page=' + str(self.per_page)
        prev_link = '/videos?query=' + str(self.query) + 'page=' + str(max(self.page - 1, 1)) + '&per_page=' + str(self.per_page)

        return next_link, prev_link
