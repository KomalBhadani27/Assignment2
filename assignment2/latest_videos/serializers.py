from rest_framework import serializers

from .models import VideoByCategory, LatestVideos, VideoCategories


class LatestVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = LatestVideos
        fields = ('id', 'title', 'desc', 'published_at')


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoByCategory
        fields = ('type_id', )


class SearchAPISerializer(serializers.ModelSerializer):
    category = TypeSerializer(many=True, )

    class Meta:
        model = LatestVideos
        fields = ('id', 'title', 'desc', 'published_at', 'thumbnails', 'channel_id', 'category')
