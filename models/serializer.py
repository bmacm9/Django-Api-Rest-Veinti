from rest_framework import serializers
from .models import User, PersonalSpace, Photo, CommentPhoto, CommentProfile, Friend, Tagged, Status

# Classes to move the information over the internet (in XML or JSON...)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

class CommentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPhoto
        fields = "__all__"

class CommentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentProfile
        fields = "__all__"

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"

class TaggedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tagged
        fields = "__all__"

class PersonalSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalSpace
        fields = "__all__"

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"