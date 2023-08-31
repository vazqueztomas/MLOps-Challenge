from typing import Annotated

from fastapi import Depends, APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter()

security = HTTPBasic()

@router.get("/")
def get_current_user(credential: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credential.username, "password": credential.password}