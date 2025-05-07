from fastapi import APIRouter
from .schemas import SearchUsersResponse, UserOut
from utils.dependencies import user_verify_dependency,psql_dependency
from utils.psql.models import User
from sqlalchemy import or_

social_actions_router = APIRouter(prefix="/social_actions", tags=["SocialActions"])

@social_actions_router.get("/search_users", response_model=SearchUsersResponse)
async def search_users(q:str, limit: int=100, offset: int=0, user_data=user_verify_dependency, psql_db=psql_dependency):
    
    users = psql_db.query(User).where(or_(User.email.contains(q), User.display_name.contains(q))).order_by(User.email.asc()).all()
    start = offset
    end = offset+limit
    return SearchUsersResponse(
        data=[UserOut.model_validate(user) for user in users[start:end]],
        next_offset=end if len(users) > end else None
    )
    