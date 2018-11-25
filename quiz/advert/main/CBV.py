from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import AdvertModelSerializer
from .models import Advert

class AdvertList(APIView):

    def get(self, request):
        adverts = Advert.objects.all()
        serializer = AdvertModelSerializer(adverts, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'please, authenticate!'})
        else:
            serializer = AdvertModelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvertDetail(APIView):

    def get_object(self, pk):
        try:
            advert = Advert.objects.get(pk=pk)
            return advert
        except advert.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        advert = self.get_object(pk)
        serializer = AdvertModelSerializer(advert)
        return Response(serializer.data)

    def put(self, request, pk):
        if not request.user.is_authenticated:
            return Response({'error': 'please, authenticate!'})
        else:
            advert = self.get_object(pk)
            serializer = AdvertModelSerializer(instance=advert, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not request.user.is_authenticated:
            return Response({'error': 'please, authenticate!'})
        else:
            advert = self.get_object(pk)
            advert.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
