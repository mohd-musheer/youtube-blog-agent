from pydantic import BaseModel


class BlogRequest(BaseModel):
    youtube_url: str