from django.urls import include, path
from rest_framework import routers

from .views import AlbumViewSet

router = routers.DefaultRouter()
router.register(r"albums", AlbumViewSet, basename="album")
urlpatterns = [path("", include(router.urls))]
