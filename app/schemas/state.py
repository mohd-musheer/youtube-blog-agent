from typing_extensions import TypedDict


class BlogState(TypedDict, total=False):

    youtube_url: str

    raw_metadata: str

    cleaned_content: str

    summary: str

    blog_title: str

    blog_content: str