from django.db import models

# Create your models here.


class LatestVideos(models.Model):
    """ Model for latest_videos Table which will store all
        the latest videos fetched from the YouTube API"""

    class Meta:
        verbose_name_plural = 'LatestVideos'

    id = models.CharField(max_length=100, primary_key=True)
    title = models.TextField()
    desc = models.TextField()
    published_at = models.DateTimeField()
    channel_id = models.CharField(max_length=100)
    thumbnails = models.JSONField()


class VideoCategories(models.Model):
    """Model for video_types table which will store
        all video types."""

    class Meta:
        verbose_name_plural = 'VideoCategories'

    id = models.CharField(max_length=200, primary_key=True)
    timestamp = models.DateTimeField()


class VideoByCategory(models.Model):
    """ Model for video_by_category table which will store
        the videos for various video types"""

    class Meta:
        verbose_name_plural = 'VideoByCategory'

    type_id = models.ForeignKey(VideoCategories, on_delete=models.CASCADE)
    video_id = models.ForeignKey(LatestVideos, related_name='category', on_delete=models.CASCADE)

