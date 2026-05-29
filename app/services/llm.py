import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY not found."
    )

model = init_chat_model(
    "groq:openai/gpt-oss-120b"
)