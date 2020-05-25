from django.db import models
from django.utils import timezone

class User(models.Model):
    ''' The model for our Users '''

    def __str__(self):
        return self.name + " " + self.surname
    
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    profile_pic = models.ImageField(null=True, blank=True)
    invitations = models.IntegerField()
    visits = models.IntegerField(default=0)
    born = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, default="Hombre")
    civilStatus = models.CharField(max_length=50, default="Soltero")

class Status(models.Model):
    status_text = models.CharField(max_length=50)
    dateTime = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hasAnswers = models.CharField(max_length=10, default="no")

class PersonalSpace(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    video = models.CharField(max_length=50, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=timezone.now)

class CommentProfile(models.Model):
    ''' The model for posting in someone else wall '''
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_requests_assigned')
    comment = models.TextField()
    hasAnswers = models.CharField(default="no", max_length=10)
    dateTime = models.DateTimeField(default=timezone.now)

class Friend(models.Model):
    ''' The model to have a user with friends '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    is_friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_requests_assigned')

class Photo(models.Model):
    ''' The model for the photos that users are tagged on '''
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=timezone.now)
    image = models.ImageField()
    title = models.CharField(null=True, max_length=50)

class CommentPhoto(models.Model):
    ''' The model to write in the photos uploaded '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Photo, on_delete=models.CASCADE)
    comment = models.TextField()
    dateTime = models.DateTimeField(default=timezone.now)

class CommentStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    comment = models.TextField()
    dateTime = models.DateTimeField(default=timezone.now)


class Tagged(models.Model):
    ''' The model for the user tagged on a photo '''
    image = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ReplyComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commentProfile = models.ForeignKey(CommentProfile, on_delete=models.CASCADE, null=True)
    commentStatus = models.ForeignKey(CommentStatus, on_delete=models.CASCADE, null=True)
    commentPhoto = models.ForeignKey(CommentPhoto, on_delete=models.CASCADE, null=True)
    reply = models.TextField()
    dateTime = models.DateTimeField(default=timezone.now)