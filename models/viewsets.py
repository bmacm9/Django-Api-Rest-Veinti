from rest_framework import viewsets, generics
from .models import User, CommentPhoto, PersonalSpace, CommentProfile, Friend, Tagged, Photo, Status
from .serializer import UserSerializer, PersonalSpaceSerializer, CommentPhotoSerializer, CommentProfileSerializer, FriendSerializer, TaggedSerializer, PhotoSerializer, StatusSerializer


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
        return queryset

class CommentPhotoViewSet(viewsets.ModelViewSet):
    queryset = CommentPhoto.objects.all()
    serializer_class = CommentPhotoSerializer

class CommentProfileViewSet(viewsets.ModelViewSet):
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
        if 'user' in query.keys():
            queryset = queryset.filter(user=query.get('user'))
            return queryset

        if 'is_friend' in query.keys():
            queryset = queryset.filter(is_friend=query.get('is_friend'))
            return queryset
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
    queryset = Status.objects.all().order_by('-dateTime')
    serializer_class = StatusSerializer

    def get_queryset(self):
        ''' Filtramos la busqueda a esta api por email y contraseña para iniciar sesion '''
        query = self.request.query_params
        queryset = self.queryset
        if 'user' in query.keys():
            queryset = queryset.filter(user=query.get('user'))
            return queryset
        return queryset