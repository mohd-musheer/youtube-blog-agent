import json

from app.services.llm import model

from app.services.youtube import (
    extract_youtube_data
)
from app.schemas.state import BlogState

from langgraph.graph import (
    StateGraph,
    START,
    END
)

def clean_metadata(state: BlogState):

    raw_data = state["raw_metadata"]

    response = model.invoke(f"""
    Clean this YouTube metadata and transcript.
    
    Focus on:
    - main topic
    - important concepts
    - remove noise
    - prioritize title and transcript
    
    DATA:
    {raw_data}
    """)

    return {
        "cleaned_content": response.content
    }

def generate_blog(state: BlogState):

    title = state["blog_title"]

    summary = state["summary"]

    response = model.invoke(f"""
        Write detailed professional blog.

        TITLE:
        {title}

        CONTENT:
        {summary}
        """)

    return {
        "blog_content": response.content
    }
    
    
def generate_blog_title(state: BlogState):

    summary = state["summary"]

    response = model.invoke(f"""
    Generate SEO friendly blog title.

    {summary}
    """)

    return {
        "blog_title": response.content
    }
    
    
def summarize_content(state: BlogState):

    content = state["cleaned_content"]

    response = model.invoke(f"""
    Summarize this content into key points.

    {content}
    """)

    return {
        "summary": response.content
    }
    
import json

def generate_blog_post(state):

    summary = state["summary"]

    response = model.invoke(f"""
        Return ONLY valid JSON.

        {{
        "title":"...",
        "content":"..."
        }}

        Write a complete blog article.

        Requirements:
        - 800-1200 words
        - Introduction
        - Main discussion
        - Conclusion
        - Professional tone
        - Paragraphs instead of bullet points

        CONTENT:
        {summary}
        """)

    content = response.content.strip()

    # Remove markdown fences if Gemini adds them
    if content.startswith("```json"):
        content = content.replace("```json", "").replace("```", "").strip()

    data = json.loads(content)

    return {
        "blog_title": data["title"],
        "blog_content": data["content"]
    }
    
from langgraph.graph import START, END,StateGraph

builder = StateGraph(BlogState)

builder.add_node("extract", extract_youtube_data)
builder.add_node("clean", clean_metadata)
builder.add_node("summarize", summarize_content)
builder.add_node("generate_post", generate_blog_post)

builder.add_edge(START, "extract")
builder.add_edge("extract", "clean")
builder.add_edge("clean", "summarize")
builder.add_edge("summarize", "generate_post")
builder.add_edge("generate_post", END)

graph = builder.compile()