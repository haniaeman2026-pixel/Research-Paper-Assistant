<div align="center">

<br>

<img src="https://readme-typing-svg.demolab.com?font=Georgia&weight=700&size=38&duration=2800&pause=900&color=7A4E35&center=true&vCenter=true&width=900&height=70&lines=Research+Paper+Assistant" alt="Research Paper Assistant" />

<br>

<img src="https://readme-typing-svg.demolab.com?font=Montserrat&weight=500&size=19&duration=2600&pause=700&color=A56F52&center=true&vCenter=true&width=850&height=45&lines=AI-Powered+Research+%26+RAG+Assistant;Upload+Papers+%E2%80%A2+Ask+Questions+%E2%80%A2+Get+Grounded+Answers" alt="Project Subtitle" />

<br><br>

<a href="https://research-paper-assistant-gules.vercel.app/">
<img src="https://img.shields.io/badge/%E2%9C%A6%20LIVE%20DEMO-7A4E35?style=for-the-badge&labelColor=2F211B" />
</a>

&nbsp;

<a href="https://github.com/haniaeman2026-pixel/Research-Paper-Assistant">
<img src="https://img.shields.io/badge/SOURCE%20CODE-9A684D?style=for-the-badge&logo=github&logoColor=white" />
</a>

<br><br>

<img src="https://img.shields.io/badge/Python-3.12-7A4E35?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square" />
<img src="https://img.shields.io/badge/LangGraph-5C4033?style=flat-square" />
<img src="https://img.shields.io/badge/Groq-F55036?style=flat-square" />
<img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white" />

<br><br>

> **Transform lengthy research papers into an interactive AI-powered knowledge experience.**

<br>

</div>

---

<div align="center">

## ✦ PROJECT OVERVIEW

</div>

**Research Paper Assistant** is a research-focused AI application built around a **Retrieval-Augmented Generation (RAG)** workflow.

It allows users to upload research papers in PDF format, ask questions in natural language, retrieve relevant content, and generate answers grounded in the uploaded research material.

The application is designed to make long and information-heavy research papers easier to explore without manually searching through every page.

<br>

<div align="center">


📄 UPLOAD
    │
    ▼
📖 EXTRACT
    │
    ▼
✂️ CHUNK
    │
    ▼
🔎 RETRIEVE
    │
    ▼
🧩 LANGGRAPH
    │
    ▼
🤖 GROQ
    │
    ▼
💬 ANSWER
    │
    ▼
📑 SOURCES
</div>
<div align="center">
✦ WHY THIS PROJECT?
</div>

Research papers can contain dozens of pages of dense technical information.

Instead of repeatedly searching through PDFs, this application provides a conversational interface where users can ask questions directly.

The Core Idea

Upload the paper → Ask a question → Retrieve relevant context → Generate a grounded answer.

This creates a more direct workflow for exploring research material.

<br>
<div align="center">
✦ KEY FEATURES
</div> <table> <tr> <td width="50%" valign="top">
📄 Research Paper Processing
PDF document upload
PDF validation
Text extraction
Multiple research-paper support
Empty-file handling
Unsupported-format handling
</td> <td width="50%" valign="top">
🔎 Context Retrieval
Relevant content retrieval
Text chunking
Research-focused context
Document metadata
Page-level information
</td> </tr> <tr> <td width="50%" valign="top">
🤖 AI Question Answering
Natural-language questions
Groq-powered generation
Context-grounded answers
Controlled generation
Fallback responses
</td> <td width="50%" valign="top">
🧩 LangGraph Workflow
Retrieval node
Relevance checking
Context preparation
Answer generation
Fallback routing
</td> </tr> <tr> <td width="50%" valign="top">
☁️ Cloud Deployment
FastAPI backend
Vercel deployment
Vercel Blob storage
Production API
</td> <td width="50%" valign="top">
📑 Source Awareness
Source document
Page information
Retrieved content
Research-focused responses
</td> </tr> </table> <br>
<div align="center">
✦ RAG ARCHITECTURE
</div>
╭────────────────────────────────────────────────────────╮
│                 RESEARCH PAPER PDF                     │
╰──────────────────────────┬─────────────────────────────╯
                           │
                           ▼
╭────────────────────────────────────────────────────────╮
│                    PDF PROCESSING                      │
│               PyPDF  •  PDFPlumber                     │
╰──────────────────────────┬─────────────────────────────╯
                           │
                           ▼
╭────────────────────────────────────────────────────────╮
│                    TEXT CHUNKING                       │
│                     LangChain                          │
╰──────────────────────────┬─────────────────────────────╯
                           │
                           ▼
╭────────────────────────────────────────────────────────╮
│                     RETRIEVAL                          │
│              Relevant Research Context                 │
╰──────────────────────────┬─────────────────────────────╯
                           │
                           ▼
╭────────────────────────────────────────────────────────╮
│                    LANGGRAPH                            │
│         Retrieve → Check → Prepare → Generate          │
╰──────────────────────────┬─────────────────────────────╯
                           │
                           ▼
╭────────────────────────────────────────────────────────╮
│                      GROQ                              │
│                 LLM Answer Generation                  │
╰──────────────────────────┬─────────────────────────────╯
                           │
                           ▼
╭────────────────────────────────────────────────────────╮
│                  FINAL RESPONSE                        │
│             Answer + Document + Page                   │
╰────────────────────────────────────────────────────────╯
<br>
<div align="center">
✦ HOW IT WORKS
</div>
01 — Upload

The user uploads one or more research papers in PDF format.

↓

02 — Extract

The application extracts readable text from the uploaded PDF using PyPDF and PDFPlumber.

↓

03 — Chunk

Extracted text is divided into smaller sections using LangChain text-splitting functionality.

↓

04 — Retrieve

When the user asks a question, relevant research content is retrieved from the indexed document content.

↓

05 — Validate Context

LangGraph checks whether relevant context is available before generating an answer.

↓

06 — Generate

The retrieved context is passed to the Groq LLM, which generates a response based on the supplied research content.

↓

07 — Return Sources

The application returns source information associated with the retrieved research content, including document and page metadata.

<br>
<div align="center">
✦ LANGGRAPH WORKFLOW
</div>
                    ┌─────────────────┐
                    │  USER QUESTION  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    RETRIEVE     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ CHECK RELEVANCE │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                  YES                 NO
                    │                 │
                    ▼                 ▼
          ┌─────────────────┐  ┌─────────────────┐
          │ PREPARE CONTEXT │  │    FALLBACK     │
          └────────┬────────┘  └─────────────────┘
                   │
                   ▼
          ┌─────────────────┐
          │  GENERATE ANSWER│
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ FINAL RESPONSE  │
          └─────────────────┘
<br>
<div align="center">
✦ TECHNOLOGY STACK
</div>
Technology	Purpose
🐍 Python	Core application development
⚡ FastAPI	Backend REST API
📄 PyPDF	PDF text extraction
📑 PDFPlumber	PDF processing
🔗 LangChain	Document processing & text splitting
🧩 LangGraph	AI workflow orchestration
🤖 Groq	LLM inference
🧠 GPT OSS 20B	Answer generation
☁️ Vercel	Cloud deployment
🗄️ Vercel Blob	PDF cloud storage
🎨 HTML / CSS / JavaScript	Frontend interface
🔬 LangSmith	Optional tracing & observability
<br>
<div align="center">
✦ PROJECT STRUCTURE
</div>
Research-Paper-Assistant/
│
├── 📁 app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── pdf_loader.py
│   ├── rag.py
│   ├── graph.py
│   ├── llm.py
│   └── blob_storage.py
│
├── 📁 api/
│   └── index.py
│
├── 📁 static/
│   ├── style.css
│   └── app.js
│
├── 📁 templates/
│   └── index.html
│
├── 📁 uploads/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
<br>
<div align="center">
✦ INSTALLATION
</div>
01 — Clone Repository
git clone https://github.com/haniaeman2026-pixel/Research-Paper-Assistant.git
02 — Open Project
cd Research-Paper-Assistant
03 — Create Virtual Environment
python -m venv venv
04 — Activate Environment

PowerShell

.\venv\Scripts\Activate.ps1

CMD

venv\Scripts\activate.bat
05 — Install Dependencies
python -m pip install -r requirements.txt
<br>
<div align="center">
✦ ENVIRONMENT CONFIGURATION
</div>

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b

LANGSMITH_TRACING=false
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=research-paper-assistant

For Vercel Blob, configure the required Blob environment variable through your Vercel project settings.

🔐 Never commit .env, API keys, access tokens, or other secrets to GitHub.

<br>
<div align="center">
✦ RUN LOCALLY
</div>

Start the application:

python -m uvicorn app.main:app --port 8001

Open:

http://127.0.0.1:8001
<br>
<div align="center">
✦ API ENDPOINTS
</div>
Method	Endpoint	Description
GET	/	Main application
GET	/api/health	Health check
POST	/api/upload	Upload & process PDFs
POST	/api/ask	Ask research questions
Health Response
{
  "status": "online",
  "service": "Research Paper Assistant",
  "version": "1.0.0"
}
<br>
<div align="center">
✦ EXAMPLE QUESTIONS
</div>
"What is the main objective of this research?"

"What methodology does the paper use?"

"What dataset was used?"

"What are the major findings?"

"What limitations are mentioned?"

"What future work is suggested?"

"What algorithm or architecture is discussed?"
<br>
<div align="center">
✦ GROUNDED AI RESPONSES
</div>

The assistant is designed around a strict context-based generation strategy.

Research Paper
      │
      ▼
Relevant Context
      │
      ▼
┌───────────────┐
│    GROQ LLM   │
└───────┬───────┘
        │
        ▼
Context-Grounded
     Answer

The generation layer is instructed to:

Use the supplied research context
Avoid unsupported claims
Avoid guessing
Avoid fabricated citations
Avoid unrelated information
Return a fallback when required information is unavailable

When the requested information cannot be found in the available research context:

The answer is not available in the uploaded research papers.
<br>
<div align="center">
✦ ERROR HANDLING
</div>

The application handles common scenarios such as:

╭────────────────────────────────────╮
│ ❌ No PDF uploaded                 │
│ ❌ Unsupported file format         │
│ ❌ Empty uploaded file             │
│ ❌ Empty question                  │
│ ❌ No relevant context             │
│ ❌ PDF processing failure          │
│ ❌ Missing API configuration       │
│ ❌ AI generation failure           │
│ ❌ Duplicate Blob filename         │
╰────────────────────────────────────╯
<br>
<div align="center">
✦ LIVE DEPLOYMENT
<br> <a href="https://research-paper-assistant-gules.vercel.app/"> <img src="https://img.shields.io/badge/%E2%9C%A6%20OPEN%20LIVE%20APPLICATION-7A4E35?style=for-the-badge&logo=vercel&logoColor=white" /> </a>

<br><br>

Production URL

<br> <a href="https://research-paper-assistant-gules.vercel.app/">

https://research-paper-assistant-gules.vercel.app/

</a> </div> <br>
<div align="center">
✦ DEPLOYMENT
</div>

The application is deployed using Vercel.

Production Deployment
vercel --prod

Uploaded research papers are stored using Vercel Blob.

<br>
<div align="center">
✦ PROJECT GOALS
</div>
📚 Simplify Research Paper Exploration

🔎 Reduce Manual PDF Searching

🤖 Apply AI to Research Workflows

🧠 Demonstrate RAG Concepts

🧩 Build Structured LLM Workflows

📑 Preserve Source Awareness

☁️ Deploy an AI Application to the Cloud
<br>
<div align="center">
✦ FUTURE IMPROVEMENTS
</div>
Planned Enhancement	Goal
🧠 Semantic Retrieval	Improve contextual matching
🔢 Embeddings	Enable similarity-based retrieval
🗄️ Vector Database	Persistent retrieval storage
📚 Advanced Multi-Document Search	Improve cross-paper retrieval
🔗 Citation Mapping	More precise source references
💬 Conversation Memory	Maintain chat context
⚡ Streaming Responses	Improve response experience
📊 Retrieval Evaluation	Measure retrieval quality
🔬 LangSmith Observability	Advanced tracing
🔐 Authentication	Secure user access
<br>
<div align="center">
✦ SKILLS DEMONSTRATED
<br>

Python · FastAPI · RAG · LLMs · LangChain · LangGraph

Prompt Engineering · PDF Processing · REST APIs

Cloud Deployment · Vercel Blob · AI Application Architecture

</div> <br>
<div align="center">
✦ DEVELOPER
<br> <img src="https://readme-typing-svg.demolab.com?font=Georgia&weight=700&size=27&duration=2600&pause=1000&color=7A4E35&center=true&vCenter=true&width=650&height=55&lines=Developed+by+Hania+Eman" alt="Developer" /> <br> <img src="https://readme-typing-svg.demolab.com?font=Montserrat&weight=500&size=17&duration=2400&pause=900&color=A56F52&center=true&vCenter=true&width=650&height=40&lines=AI+%26+Data+Science+Student;ML+Developer+%7C+Python+Enthusiast" alt="Developer Role" />

<br><br>

<a href="https://github.com/haniaeman2026-pixel"> <img src="https://img.shields.io/badge/GitHub-Hania%20Eman-2F211B?style=for-the-badge&logo=github&logoColor=white" /> </a> </div> <br>
<div align="center"> <img src="https://readme-typing-svg.demolab.com?font=Georgia&weight=600&size=22&duration=2600&pause=900&color=7A4E35&center=true&vCenter=true&width=750&height=45&lines=Research+Smarter.+Understand+Faster.;Built+for+Research-Focused+AI+Workflows." alt="Closing Animation" />

<br><br>

Research Paper Assistant

<br>

Python · FastAPI · LangChain · LangGraph · Groq · Vercel

<br><br>

Developed by Hania Eman

<br><br>

</div> ```
