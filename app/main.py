from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.graph.workflow import graph

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


class BlogRequest(BaseModel):
    youtube_url: str


@app.post("/generate-blog")
def generate_blog(request: BlogRequest):

    result = graph.invoke(
        {
            "youtube_url": request.youtube_url
        }
    )

    return {
        "title": result["blog_title"],
        "content": result["blog_content"]
    }