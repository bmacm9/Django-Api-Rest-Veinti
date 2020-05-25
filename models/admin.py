from django.contrib import admin

#Register models into django admin

from .models import User, Photo, CommentPhoto, CommentProfile, Friend, Tagged, PersonalSpace, Status, CommentStatus, ReplyComment

admin.site.register(User)
admin.site.register(Photo)
admin.site.register(CommentProfile)
admin.site.register(CommentPhoto)
admin.site.register(Friend)
admin.site.register(Tagged)
admin.site.register(PersonalSpace)
admin.site.register(Status)
admin.site.register(CommentStatus)
admin.site.register(ReplyComment)