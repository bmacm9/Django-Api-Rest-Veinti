from rest_framework import routers

from .viewsets import UserViewSet, PersonalSpaceViewSet, PhotoViewSet, CommentPhotoViewSet, CommentProfileViewSet, FriendViewSet, TaggedViewSet, StatusViewSet, ReplyCommentViewSet, CommentStatusViewSet

router = routers.SimpleRouter()

router.register('users', UserViewSet)
router.register('photos', PhotoViewSet)
router.register('commentphotos', CommentPhotoViewSet)
router.register('commentsprofiles', CommentProfileViewSet)
router.register('friends', FriendViewSet)
router.register('tagged', TaggedViewSet)
router.register('personalspace', PersonalSpaceViewSet)
router.register('status', StatusViewSet)
router.register('replycomment', ReplyCommentViewSet)
router.register('commentstatus', CommentStatusViewSet)

urlpatterns = router.urls