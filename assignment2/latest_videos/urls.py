from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'latestvideos', views.LatestVideosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('videos/', views.SearchVideosViewSet.as_view()),
    path('api-auth', include('rest_framework.urls',
                             namespace='rest_framework'))
]
