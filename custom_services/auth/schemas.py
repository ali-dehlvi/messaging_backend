from pydantic import BaseModel, Field
from typing import Optional

class CreateUserModel(BaseModel):
    email: str = Field(description="Email of the user")
    password: str = Field(description="Password of the user")
    display_name: str = Field(description="Full name of the user")
    email_verified: Optional[bool] = Field(default=False, description="Default Email verified")


class DeleteUserModel(BaseModel):
    email: str = Field(description="Email to delete")


class BaseResponseModel(BaseModel):
    success: bool = Field(description="True if API is runs without any error")
    message: Optional[str] = Field(description="Message related to API's success and failure")


class BulkCreateUsersRequest(BaseModel):
    users: list[CreateUserModel]

class BulkDeleteUsersRequest(BaseModel):
    users: list[CreateUserModel]


class BulkBaseResponseModel(BaseModel):
    result: list[BaseResponseModel]
