from yt_dlp import YoutubeDL
from yt_dlp import YoutubeDL
from urllib.parse import urlparse, parse_qs

from app.schemas.state import BlogState

from youtube_transcript_api import YouTubeTranscriptApi

def extract_youtube_data(state: BlogState):
    """
    Takes YouTube URL and returns:
    - title
    - description
    - transcript
    """

    # -------- Extract Metadata --------

    with YoutubeDL({}) as ydl:
        info = ydl.extract_info(state['youtube_url'], download=False)

    title = info.get("title", "")
    description = info.get("description", "")

    # -------- Extract Video ID --------


    parsed_url = urlparse(state['youtube_url'])

    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        video_id = parse_qs(parsed_url.query).get("v", [None])[0]

    if parsed_url.hostname == "youtu.be":
        video_id = parsed_url.path[1:]

    if not video_id:
        return "Invalid YouTube URL"

    # -------- Get Transcript --------

    try:
        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        transcript_text = " ".join([x.text for x in transcript])

    except Exception as e:

        transcript_text = f"Transcript not available: {str(e)}"

    # -------- Final Combined Output --------

    final_text = f"""
        TITLE:
        {title}

        DESCRIPTION:
        {description}

        TRANSCRIPT:
        {transcript_text}
        """

    return {
        "raw_metadata": final_text
    }