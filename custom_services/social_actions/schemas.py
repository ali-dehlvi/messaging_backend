

from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from utils.psql.models import User


class UserOut(BaseModel):
    email: str
    display_name: str
    phone: Optional[str]

    model_config = ConfigDict(from_attributes=True)

class SearchUsersResponse(BaseModel):
    data: List[UserOut]
    next_offset: int | None
