from rest_framework import viewsets, generics
from .models import User, CommentPhoto, PersonalSpace, CommentProfile, Friend, Tagged, Photo, Status, ReplyComment, CommentStatus, FriendRequest, PrivateMessage, Invitation
from .serializer import UserSerializer, PersonalSpaceSerializer, CommentPhotoSerializer, CommentProfileSerializer, FriendSerializer, TaggedSerializer, PhotoSerializer, StatusSerializer, ReplyCommentSerializer, CommentStatusSerializer, FriendRequestSerializer, PrivateMessageSerializer, InvitationSerializer
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        ''' Filtramos la busqueda a esta api por email y contraseña para iniciar sesion '''
        query = self.request.query_params
        queryset = self.queryset

        if 'email' and 'password' in query.keys():
            queryset = queryset.filter(email=query.get('email'), password=query.get('password'))
            return queryset

        if 'email' in query.keys():
            queryset = queryset.filter(email=query.get('email'))
            return queryset

        if 'id' in query.keys():
            queryset = queryset.filter(id=query.get('id'))
            return queryset

        if 'name' and 'surname' in query.keys():
            queryset = queryset.filter(name=query.get('name'), surname=query.get('surname'))
            return queryset

        if 'name' in query.keys():
            queryset = queryset.filter(name=query.get('name'))
            return queryset

        if 'surname' in query.keys():
            queryset = queryset.filter(surname=query.get('surname'))
            return queryset
        return queryset

class CommentPhotoViewSet(viewsets.ModelViewSet):
    queryset = CommentPhoto.objects.all()
    serializer_class = CommentPhotoSerializer

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset

        if 'image' in query.keys():
            queryset = queryset.filter(image=query.get('image'))
            return queryset
        return queryset

class CommentProfileViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = CommentProfile.objects.all().order_by('-dateTime')
    serializer_class = CommentProfileSerializer

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'profile' in query.keys():
            queryset = queryset.filter(profile=query.get('profile'))
            return queryset
        return queryset

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset


        if 'is_friend' in query.keys():
            queryset = queryset.filter(is_friend=query.get('is_friend'))
            return queryset


        if 'user' in query.keys():
            queryset = queryset.filter(user=query.get('user'))
            return queryset
        return queryset

        if 'user' and 'is_friend' in query.keys():
            queryset = queryset.filter(user=query.get('user'), is_friend=query.get('is_friend'))
            return queryset


class TaggedViewSet(viewsets.ModelViewSet):
    queryset = Tagged.objects.all()
    serializer_class = TaggedSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('-dateTime')
    serializer_class = PhotoSerializer

    def get_queryset(self):
        ''' Filtramos la busqueda a esta api por email y contraseña para iniciar sesion '''
        query = self.request.query_params
        queryset = self.queryset
        if 'uploaded_by' in query.keys():
            queryset = queryset.filter(uploaded_by=query.get('uploaded_by'))
            return queryset
        return queryset

class PersonalSpaceViewSet(viewsets.ModelViewSet):
    queryset = PersonalSpace.objects.all().order_by('-dateTime')
    serializer_class = PersonalSpaceSerializer

    def get_queryset(self):
        ''' Filtramos la busqueda a esta api por email y contraseña para iniciar sesion '''
        query = self.request.query_params
        queryset = self.queryset
        if 'user' in query.keys():
            queryset = queryset.filter(user=query.get('user'))
            return queryset
        if 'id' in query.keys():
            queryset = queryset.filter(id=query.get('id'))
            return queryset
        return queryset

class StatusViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Status.objects.all().order_by('-dateTime')
    serializer_class = StatusSerializer

    def get_queryset(self):
        ''' Filtramos la busqueda a esta api por email y contraseña para iniciar sesion '''
        query = self.request.query_params
        queryset = self.queryset
        if 'user' in query.keys():
            queryset = queryset.filter(user=query.get('user'))
            return queryset
        if 'id' in query.keys():
            queryset = queryset.filter(id=query.get('id'))
            return queryset
        return queryset

class CommentStatusViewSet(viewsets.ModelViewSet):
    queryset = CommentStatus.objects.all().order_by('-dateTime')
    serializer_class = CommentStatusSerializer

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'status' in query.keys():
            queryset = queryset.filter(status=query.get('status'))
            return queryset
        return queryset

class ReplyCommentViewSet(viewsets.ModelViewSet):
    queryset = ReplyComment.objects.all().order_by('-dateTime')
    serializer_class = ReplyCommentSerializer
    
    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'commentProfile' in query.keys():
            queryset = queryset.filter(commentProfile=query.get('commentProfile'))
            return queryset
        return queryset

class FriendRequestViewSets(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'send_to' in query.keys():
            queryset = queryset.filter(send_to=query.get('send_to'))
            return queryset
        return queryset

class PrivateMessageViewSets(viewsets.ModelViewSet):
    queryset = PrivateMessage.objects.all().order_by('-dateTime')
    serializer_class = PrivateMessageSerializer

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'send_to' in query.keys():
            queryset = queryset.filter(send_to=query.get('send_to'))
            return queryset

        if 'user' in query.keys():
            queryset = queryset.filter(user=query.get('user'))
            return queryset

        if 'user' and 'send_to' in query.keys():
            queryset = queryset.filter(user=query.get('user'), send_to=query.get('send_to'))
            return queryset
        return queryset

class InvitationViewSets(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'code' in query.keys():
            queryset = queryset.filter(code=query.get('code'))
            return queryset
        return queryset