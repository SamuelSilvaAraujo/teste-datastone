from django.urls import path

from api.views import ConverterApiView

app_name = "api"


urlpatterns = [
    path("", ConverterApiView.as_view(), name="converter"),
]
