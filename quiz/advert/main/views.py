from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .serializer import AdvertModelSerializer
from .models import Advert
from django.contrib.auth.decorators import login_required

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid data', 'username': request.data, 'password': password})

    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

@login_required 
@api_view(['GET', 'POST'])
def advert_list(request, format=None):
    if request.method == 'GET':
        advert = Advert.objects.all()
        serializer = AdvertModelSerializer(advert, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdvertModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def advert_detail(request, pk):
    try:
        advert = Advert.objects.get(pk=pk)
    except advert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertModelSerializer(advert)
        advert.number_of_views += 1
        advert.save()
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AdvertModelSerializer(instance=advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
