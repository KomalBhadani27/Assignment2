from rest_framework import serializers

from .models import VideoByCategory, LatestVideos, VideoCategories


class LatestVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = LatestVideos
        fields = '__all__'
