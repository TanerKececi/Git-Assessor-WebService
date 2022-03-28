from fastapi import Depends, APIRouter
from github import Github

from src.model.git_link import Git_Links
from ..service.check_links_service import check_links_service

assessor_router = APIRouter()

@assessor_router.get("/")
def read_item(link = Depends(Git_Links)):
    return check_links_service(link)