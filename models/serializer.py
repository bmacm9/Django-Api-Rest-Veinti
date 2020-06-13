from rest_framework import serializers
from .models import User, PersonalSpace, Photo, CommentPhoto, CommentProfile, Friend, Tagged, Status, CommentStatus, ReplyComment, FriendRequest, PrivateMessage, Invitation, Notifications

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

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        self.fields['is_friend'] = UserSerializer(read_only=True)
        return super(FriendSerializer, self).to_representation(instance)

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

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        self.fields['send_to'] = UserSerializer(read_only=True)
        return super(FriendRequestSerializer, self).to_representation(instance)

class PrivateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateMessage
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        self.fields['send_to'] = UserSerializer(read_only=True)
        return super(PrivateMessageSerializer, self).to_representation(instance)

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        return super(InvitationSerializer, self).to_representation(instance)

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        return super(NotificationsSerializer, self).to_representation(instance)