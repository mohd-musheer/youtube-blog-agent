from yt_dlp import YoutubeDL
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

from app.schemas.state import BlogState


def extract_youtube_data(state: BlogState):
    """
    Takes YouTube URL and returns:
    - title
    - description
    - transcript

    Works even if:
    - yt-dlp metadata extraction fails
    - transcript is unavailable
    """

    title = ""
    description = ""

    # ---------- Extract Metadata ----------

    try:

        with YoutubeDL({}) as ydl:
            info = ydl.extract_info(
                state["youtube_url"],
                download=False
            )

        title = info.get("title", "")
        description = info.get("description", "")

    except Exception as e:

        print(
            f"Metadata extraction failed: {e}"
        )

        title = ""
        description = ""

    # ---------- Extract Video ID ----------

    video_id = None

    try:

        parsed_url = urlparse(
            state["youtube_url"]
        )

        if parsed_url.hostname in [
            "www.youtube.com",
            "youtube.com"
        ]:

            video_id = parse_qs(
                parsed_url.query
            ).get("v", [None])[0]

        elif parsed_url.hostname == "youtu.be":

            video_id = parsed_url.path[1:]

    except Exception as e:

        print(
            f"Video ID extraction failed: {e}"
        )

    if not video_id:

        return {
            "raw_metadata":
            """
            TITLE:

            DESCRIPTION:

            TRANSCRIPT:
            Invalid YouTube URL
            """
        }

    # ---------- Extract Transcript ----------

    transcript_text = ""

    try:

        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        transcript_text = " ".join(
            [item.text for item in transcript]
        )

    except Exception as e:

        print(
            f"Transcript extraction failed: {e}"
        )

        transcript_text = ""

    # ---------- Fallback Handling ----------

    if not title:
        title = "Title Not Available"

    if not description:
        description = "Description Not Available"

    if not transcript_text:
        transcript_text = (
            "Transcript Not Available"
        )

    # ---------- Final Combined Text ----------

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