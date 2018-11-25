from rest_framework import serializers
from main.models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	username = serializers.CharField(max_length=300)
	email = serializers.EmailField()
	is_staff = serializers.BooleanField()

class PostSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(max_length=200)
	main_text = serializers.CharField(max_length=1000)
	author = UserSerializer(read_only=True)

	def create(self, validated_data):
		post = Post(**validated_data)
		post.author = User.objects.first()
		post.save()
		return post

	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.main_text = validated_data.get('main_text', instance.main_text)
		return instance

class PostModelSerializer(serializers.ModelSerializer):
	author = UserSerializer(read_only=True)

	class Meta:
		model = Post
		fields = ['id', 'title', 'main_text', 'author']

class CommentSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	content = serializers.CharField(max_length=500)
	rating = serializers.IntegerField()
	user = UserSerializer(read_only=True)

	def create(self, validated_data):
		post_id = validated_data.pop('post_id')
		post = Post.objects.get(pk=post_id)
		comment = Comment(**validated_data)
		comment.post = post
		comment.save()
		return comment