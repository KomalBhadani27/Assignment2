"""This script will create an API to fetch the details
    of latest videos based on a particular query."""

import datetime
import os

from celery.decorators import task
from googleapiclient.discovery import build

from .models import LatestVideos, VideoByCategory, VideoCategories

API_KEY = os.environ.get('API_KEY')
# Default timestamp if predefined query is encountered for the first time.
DEFAULT_LAST_TIMESTAMP = '2020-10-01T00:00:00Z'


@task(name="fetch_latest_videos")
def fetch_latest_videos(query):
    """This method calls youtube data API to search videos
       with given query(keyword) and store it in the database."""

    # Fetch the last time when the database was updated for given query.
    last_timestamp = __get_last_call_time(query)

    results = __fetch_from_youtube_api(query, last_timestamp)

    __add_results_to_db(results, query)

    return True


def __get_last_call_time(query):
    """Get last time when database was updated for this keyword"""

    if VideoCategories.objects.filter(pk=str(query)).exists():
        vc = VideoCategories.objects.get(id=query)
        timestamp = vc.timestamp

        return timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")

    vc = VideoCategories.objects.create(id=query,
                                        timestamp=DEFAULT_LAST_TIMESTAMP)
    vc.save()

    return DEFAULT_LAST_TIMESTAMP


def __fetch_from_youtube_api(query, last_timestamp):
    """This method requests youtube search api with given query"""

    youtube_object = build(serviceName='youtube', version='v3', developerKey=API_KEY)

    keyword = youtube_object.search().list(q=query,
                                           part="id, snippet",
                                           publishedAfter=last_timestamp,
                                           type='videos').execute()
    return keyword.get("items", [])


def __add_results_to_db(results, query):

    type_id = VideoCategories.objects.get(id=query)

    for result in results:
        videoId = None
        if 'videoId' not in result['id'].keys():
            continue

        if not LatestVideos.objects.filter(pk=result['id']['videoId']).exists():
            videoId = LatestVideos.objects.create(
                id=result['id']['videoId'],
                title=result['snippet']['title'],
                desc=result['snippet']['description'],
                published_at=result['snippet']['publishedAt'],
                channel_id=result['snippet']['channelId'],
                thumbnails=result['snippet']['thumbnails'])

            videoId.save()

        if not VideoByCategory.objects.filter(type_id=type_id,
                                              video_id=LatestVideos(id=result['id']['videoId'])).exists():
            vbc = VideoByCategory.objects. \
                create(type_id=VideoCategories(id=query),
                       video_id=LatestVideos(id=result['id']['videoId']))

            vbc.save()

    vc = VideoCategories.objects.get(id=query)
    vc.timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    vc.save()
