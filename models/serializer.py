from rest_framework import serializers
from .models import User, PersonalSpace, Photo, CommentPhoto, CommentProfile, Friend, Tagged, Status, CommentStatus, ReplyComment

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

    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(CommentPhotoSerializer, self).to_representation(instance)

class CommentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentProfile
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(CommentProfileSerializer, self).to_representation(instance)

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

    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(StatusSerializer, self).to_representation(instance)

class CommentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentStatus
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['status'] =  StatusSerializer(read_only=True)
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(CommentStatusSerializer, self).to_representation(instance)

class ReplyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyComment
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['commentProfile'] =  CommentProfileSerializer(read_only=True)
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(ReplyCommentSerializer, self).to_representation(instance)