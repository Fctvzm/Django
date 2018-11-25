from rest_framework import serializers
from .models import Advert
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	username = serializers.CharField(max_length=300)


class AdvertModelSerializer(serializers.ModelSerializer):
	owner = UserSerializer(read_only=True)

	class Meta:
		model = Advert
		fields = '__all__'