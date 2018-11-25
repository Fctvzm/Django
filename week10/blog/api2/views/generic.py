from rest_framework import generics

from api2.serializers import PostModelSerializer
from main.models import Post
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class IsSuperAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class GenericPostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Post.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GenericPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'pk'

    def get_object(self):
        return Post.objects.get(pk=self.kwargs[self.lookup_field])

    def get_queryset(self):
        return Post.objects.for_user(self.request.user)