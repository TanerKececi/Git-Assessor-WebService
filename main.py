from fastapi import FastAPI
from github import Github
from fastapi.middleware.cors import CORSMiddleware

from src.routers.git_assessor_routes import assessor_router

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    assessor_router,
    prefix="/git_assessor",
)
