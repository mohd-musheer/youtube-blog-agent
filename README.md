# 🚀 AI Blog Generator

Transform any YouTube video into a professional blog post using AI.

This project uses:

* FastAPI
* LangGraph
* Groq
* GPT-OSS-120B (`openai/gpt-oss-120b`)
* yt-dlp
* YouTube Transcript API
* Docker

The application extracts YouTube metadata and transcripts, processes the content through an AI workflow, and generates a structured blog article with a title and formatted content.

---

# ✨ Features

* Generate blogs from YouTube videos
* FastAPI REST API
* Interactive Web UI
* Dockerized deployment
* LangGraph workflow orchestration
* Markdown blog generation
* Swagger API documentation
* Ready for AWS deployment

---

# 🏗️ Architecture

```text
YouTube URL
     │
     ▼
Metadata + Transcript Extraction
     │
     ▼
Content Cleaning
     │
     ▼
Blog Generation
     │
     ▼
FastAPI Response
```

---

# 📂 Project Structure

```text
youtube-blog-agent/
│
├── app/
│   ├── agents/
│   ├── graph/
│   ├── schemas/
│   ├── services/
│   ├── static/
│   └── main.py
│
├── tests/
│
├── Dockerfile
├── requirements.txt
├── .dockerignore
└── README.md
```

---

# 🧠 AI Model

This project uses:

```text
groq:openai/gpt-oss-120b
```

through the Groq API.

---

# 🔑 Environment Variables

Required:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

https://console.groq.com

---

# 🐳 Run Using Docker

Pull image:

```bash
docker pull musheer/youtube-blog-agent
```

Run container:

```bash
docker run \
-p 8000:8000 \
-e GROQ_API_KEY=YOUR_GROQ_API_KEY \
musheer/youtube-blog-agent
```

Windows PowerShell:

```powershell
docker run `
-p 8000:8000 `
-e GROQ_API_KEY=YOUR_GROQ_API_KEY `
musheer/youtube-blog-agent
```

---

# 🌐 Access Application

Web Interface:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

OpenAPI Schema:

```text
http://localhost:8000/openapi.json
```

---

# 📡 API Usage

## Generate Blog

### Endpoint

```http
POST /generate-blog
```

### Request

```json
{
  "youtube_url": "https://youtu.be/example"
}
```

### Response

```json
{
  "title": "Generated Blog Title",
  "content": "Generated blog content..."
}
```

---

# 💻 Local Development

Clone repository:

```bash
git clone https://github.com/your-username/youtube-blog-agent.git
```

Move into project:

```bash
cd youtube-blog-agent
```

Create environment:

```bash
python -m venv .venv
```

Activate environment:

Linux/Mac:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`:

```env
GROQ_API_KEY=your_groq_api_key
```

Run:

```bash
uvicorn app.main:app --reload
```

---

# 🛠️ Tech Stack

* Python
* FastAPI
* LangGraph
* Groq
* GPT-OSS-120B
* yt-dlp
* YouTube Transcript API
* HTML
* CSS
* JavaScript
* Docker

---

# 🔮 Future Improvements

* AWS Deployment
* PostgreSQL Integration
* Redis Caching
* User Authentication
* Blog Export (PDF/DOCX)
* Multi-Language Support
* Blog History Dashboard

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Mohd. Musheer

Built with FastAPI, LangGraph, and Groq.
