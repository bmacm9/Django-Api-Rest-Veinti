from rest_framework import routers

from .viewsets import UserViewSet, PersonalSpaceViewSet, PhotoViewSet, CommentPhotoViewSet, CommentProfileViewSet, FriendViewSet, TaggedViewSet, StatusViewSet, ReplyCommentViewSet, CommentStatusViewSet, FriendRequestViewSets, PrivateMessageViewSets, InvitationViewSets, NotificationsViewSets

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
router.register('friendrequest', FriendRequestViewSets)
router.register('privatemessage', PrivateMessageViewSets)
router.register('invitation', InvitationViewSets)
router.register('notifications', NotificationsViewSets)

urlpatterns = router.urls