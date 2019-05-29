from friendship.models import FriendshipRequest

def recieved_request_processor(request):
    if not request.user.is_anonymous:
        friend_requests = list(FriendshipRequest.objects.select_related("from_user", "to_user").filter(to_user=request.user))
    else:
        friend_requests = None
    return {'friend_requests':friend_requests}