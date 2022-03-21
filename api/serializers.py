from rest_framework import serializers
from .models import Profile, FeedDataModel


class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class FeedDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedDataModel
        fields = "__all__"
