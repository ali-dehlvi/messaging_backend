from datetime import datetime
from enum import Enum
from typing import List, Literal, Optional
from pydantic import BaseModel

from utils.models import BaseResponseModel, PaginatedRequestModel, PaginatedResponseModel

class SendFriendRequest(BaseModel):
    email: str

class SendFriendRequestResponse(BaseResponseModel):
    pass


class FriendRequestStatus(Enum):
    ACCEPTED="accepted"
    REJECTED="rejected"
    PENDING="pending"
    REMOVED="removed"


class FriendRequestAnswerRequest(BaseModel):
    email: str
    status: Literal[FriendRequestStatus.ACCEPTED, FriendRequestStatus.REJECTED]

class FriendRequestAnswerResponse(BaseResponseModel):
    pass


class FriendRequestRemoveRequest(BaseModel):
    email: str

class FriendRequestRemoveResponse(BaseResponseModel):
    pass


class FriendsListRequest(BaseModel, PaginatedRequestModel):
    status: List[FriendRequestStatus]

class UserPreview(BaseModel):
    email: str
    display_name: str
    phone: Optional[str]

class FriendRequestDetail(BaseModel):
    status: str
    created_at: datetime
    updated_at: datetime
    responded_at: Optional[datetime]
    requester: UserPreview
    recipient: UserPreview

class FriendsListResponse(PaginatedResponseModel[FriendRequestDetail]):
    pass


class FriendWithMessageOut(BaseModel):
    id: int
    email: str
    display_name: str
    friend_since: datetime
    last_message: Optional[str]
    last_activity_time: datetime

class FriendsWithMessageRequest(PaginatedRequestModel):
    q: str | None
    pass

class FriendsWithMessageResponse(PaginatedResponseModel[FriendWithMessageOut]):
    pass