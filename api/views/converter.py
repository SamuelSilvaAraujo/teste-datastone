from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.serializers import ConverterSerializer


class ConverterApiView(GenericAPIView):
    serializer_class = ConverterSerializer

    def post(self, request, *args, **kwargs):
        return self.cenverter(request, *args, **kwargs)

    def cenverter(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
