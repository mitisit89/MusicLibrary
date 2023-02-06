from typing import Any

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import Artist
from .serializers import ArtistSerializer


class AlbumViewSet(viewsets.GenericViewSet):
    queryset = Artist.objects.prefetch_related("albums", "tracks").all()
    parser_classes = (JSONParser,)
    serializer_class = ArtistSerializer

    def list(self, request: Request) -> Response:
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request: Request) -> Response:
        pass
