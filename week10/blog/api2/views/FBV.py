from main.models import Post
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api2.serializers import PostModelSerializer


@api_view(['GET', 'POST'])
def posts_list(request, format=None):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostModelSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostModelSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostModelSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
