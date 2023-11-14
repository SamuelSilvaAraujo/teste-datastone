from django.urls import include, path

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("api/", include("api.urls", namespace="api")),
]
