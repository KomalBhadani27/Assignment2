from django.contrib import admin
from .models import LatestVideos, VideoCategories, VideoByCategory

# Register your models here.

admin.site.register(LatestVideos)
admin.site.register(VideoCategories)
admin.site.register(VideoByCategory)
