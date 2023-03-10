from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from library import urls as library_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "docs/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "docs",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("", include(library_urls)),
]
