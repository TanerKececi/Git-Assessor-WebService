from fastapi import Depends, APIRouter
from github import Github

from src.model.git_link import Git_Links
from ..service.check_links_service import check_links_service

assessor_router = APIRouter()

# @assessor_router.get("/{org_name}/{repo_name}")
# def check_link(link = Depends(Git_Links)):
    
#     access_token = "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"

#     g = Github(access_token)

#     repo = g.get_repo(org_name + "/" + repo_name)

#     #return check_links_service(link)


@assessor_router.get("/")
def read_item(link = Depends(Git_Links)):
    return check_links_service(link)