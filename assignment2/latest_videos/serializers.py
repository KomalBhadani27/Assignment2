from rest_framework import serializers

from .models import LatestVideos


class LatestVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LatestVideos
        fields = ('id',)
