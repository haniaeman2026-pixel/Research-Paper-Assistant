<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=34&duration=2500&pause=800&color=8B5E3C&center=true&vCenter=true&width=850&lines=Research+Paper+Assistant;AI-Powered+RAG+Research+Assistant;Ask+Questions.+Get+Grounded+Answers." alt="Research Paper Assistant Animation" />

<br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&duration=2200&pause=700&color=A66A4C&center=true&vCenter=true&width=750&lines=Upload+Research+Papers;Retrieve+Relevant+Context;Generate+AI-Powered+Answers;Track+Document+%26+Page+Sources" alt="Feature Animation" />

<br><br>

<a href="https://research-paper-assistant-gules.vercel.app/">
<img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-8B5E3C?style=for-the-badge&labelColor=3B2A22" />
</a>

<img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge" />
<img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge" />
<img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge" />
<img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" />

<br><br>

### 📚 Research Faster. Ask Smarter. Understand Better.

<p>
An AI-powered research assistant that allows users to upload research papers,
<br>
ask questions in natural language, and receive context-grounded answers
<br>
with document and page-level source information.
</p>

</div>

---

# 📖 About The Project

**Research Paper Assistant** is an AI-powered **Retrieval-Augmented Generation (RAG)** application built for interacting with research papers.

Instead of manually searching through lengthy PDF documents, users can upload their research papers and ask questions directly.

The application:


📄 Upload Research Paper
        ↓
📖 Extract PDF Content
        ↓
✂️ Split Content into Chunks
        ↓
🔎 Retrieve Relevant Context
        ↓
🧩 LangGraph Workflow
        ↓
🤖 Groq LLM
        ↓
💬 Generate Grounded Answer
        ↓
📑 Show Document & Page Sources

The assistant is designed to keep answers grounded in the uploaded research-paper content rather than intentionally relying on unrelated external information.

✨ Features
<div align="center">
Feature	Description
📄 PDF Upload	Upload research papers in PDF format
📚 Multiple Papers	Supports multiple research documents
🔎 Context Retrieval	Finds relevant content from uploaded papers
🤖 AI Answers	Generates answers using Groq
🧩 LangGraph Workflow	Structured retrieval and generation pipeline
📑 Source Tracking	Shows document and page information
🛡️ Grounded Responses	Answers are generated from retrieved paper context
⚠️ Error Handling	Handles invalid files, empty questions and missing context
☁️ Cloud Storage	Uses Vercel Blob for uploaded PDF storage
🚀 Vercel Deployment	Production-ready cloud deployment
</div>

🧠 RAG Architecture

The project follows a Retrieval-Augmented Generation workflow.

                         USER
                          │
                          ▼
                ┌──────────────────┐
                │   Upload PDF     │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   PDF Parsing    │
                │ PyPDF / PDFPlumber│
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │  Text Chunking   │
                │    LangChain     │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    Retrieval     │
                │ Relevant Chunks  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    LangGraph     │
                │ Workflow Routing │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │     Groq LLM     │
                │ Answer Generation│
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Answer + Sources │
                └──────────────────┘
🔄 How The System Works
1️⃣ Upload

The user uploads one or more research-paper PDFs.

2️⃣ Extract

The application extracts text from the PDF using:

PyPDF
PDFPlumber
3️⃣ Chunk

Large amounts of extracted text are divided into manageable chunks using LangChain's text-splitting functionality.

4️⃣ Retrieve

When a user asks a question, relevant chunks from the uploaded research content are retrieved.

5️⃣ Check Relevance

LangGraph evaluates whether relevant research context is available.

             User Question
                   │
                   ▼
              Retrieval
                   │
                   ▼
           Relevance Check
             /          \
           YES            NO
            │              │
            ▼              ▼
       Prepare Context   Fallback
            │
            ▼
       Generate Answer
6️⃣ Generate

Relevant context is passed to the Groq-powered LLM.

The model is instructed to:

Use only the supplied research context
Avoid unsupported claims
Avoid guessing
Avoid inventing information
Return a fallback when the required information is unavailable

7️⃣ Sources

The application returns source information associated with the retrieved content, including:

📄 Document name
📑 Page number
🛠️ Technology Stack
<div align="center">
Technology	Role
🐍 Python	Core programming language
⚡ FastAPI	Backend API framework
📄 PyPDF	PDF text extraction
📑 PDFPlumber	PDF processing
🔗 LangChain	Document processing & text splitting
🧩 LangGraph	Workflow orchestration
🤖 Groq	LLM inference
🧠 GPT OSS 20B	Answer generation
☁️ Vercel	Deployment
🗄️ Vercel Blob	PDF cloud storage
🎨 HTML/CSS/JavaScript	Frontend
🔬 LangSmith	Optional tracing & observability
</div>

📁 Project Structure
Research-Paper-Assistant/
│
├── app/
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
├── api/
│   └── index.py
│
├── static/
│   ├── style.css
│   └── app.js
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

⚙️ Installation
1. Clone Repository
git clone https://github.com/haniaeman2026-pixel/Research-Paper-Assistant.git
3. Enter Project Directory
cd Research-Paper-Assistant
4. Create Virtual Environment
python -m venv venv
5. Activate Environment
Windows PowerShell
.\venv\Scripts\Activate.ps1
Windows CMD
venv\Scripts\activate.bat
6. Install Dependencies
python -m pip install -r requirements.txt

🔐 Environment Variables

Create a .env file in the project root.

GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b

LANGSMITH_TRACING=false
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=research-paper-assistant

For Vercel Blob, configure the required Blob environment variable through the Vercel project environment settings.

⚠️ Never commit .env, API keys, tokens, or other secrets to GitHub.

▶️ Run Locally

Start the FastAPI server:

python -m uvicorn app.main:app --port 8001

Open:

http://127.0.0.1:8001
🔌 API Endpoints
Method	Endpoint	Purpose
GET	/	Main web application
GET	/api/health	Application health check
POST	/api/upload	Upload and process PDFs
POST	/api/ask	Ask questions about research papers
Health Check
GET /api/health

Example:

{
  "status": "online",
  "service": "Research Paper Assistant",
  "version": "1.0.0"
}
💬 Example Questions

After uploading a research paper, users can ask:

What is the main objective of this research?

What methodology does the paper use?

What dataset was used?

What are the major findings?

What limitations are mentioned?

What future work is suggested?

What algorithm or architecture is discussed?
🛡️ Grounded AI Responses

The assistant uses a strict context-based generation strategy.

┌──────────────────────────┐
│    Research Paper        │
└────────────┬─────────────┘
             │
             ▼
      Relevant Context
             │
             ▼
      ┌──────────────┐
      │   Groq LLM   │
      └──────┬───────┘
             │
             ▼
     Context-Grounded
          Answer

The generation prompt instructs the model to avoid:

❌ Unsupported facts
❌ Guessing
❌ Fabricated citations
❌ Information outside the provided context

If the requested information is not available in the retrieved research context, the application returns:

The answer is not available in the uploaded research papers.
⚠️ Error Handling

The application handles:

❌ No PDF uploaded
❌ Unsupported file format
❌ Empty uploaded file
❌ Empty user question
❌ No relevant research context
❌ PDF processing errors
❌ Missing API configuration
❌ AI generation errors
❌ Duplicate Blob filenames

This provides a more controlled user experience during document processing and question answering.

☁️ Deployment

The application is deployed on Vercel.

<div align="center">
🚀 Live Application
<a href="https://research-paper-assistant-gules.vercel.app/"> <img src="https://img.shields.io/badge/OPEN%20LIVE%20APP-Research%20Paper%20Assistant-8B5E3C?style=for-the-badge&logo=vercel&logoColor=white" /> </a>

<br><br>

<a href="https://research-paper-assistant-gules.vercel.app/">

https://research-paper-assistant-gules.vercel.app/

</a> </div>
Production Deployment
vercel --prod

The application uses Vercel Blob for cloud storage of uploaded research PDFs.

📊 Application Workflow
┌──────────────────────────────────────────────┐
│              RESEARCH PAPER                 │
│                   PDF                        │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│              PDF PROCESSING                 │
│         PyPDF + PDFPlumber                  │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│               TEXT CHUNKING                 │
│                 LangChain                   │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                RETRIEVAL                    │
│         Relevant Research Content           │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                LANGGRAPH                    │
│       Retrieve → Check → Generate           │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                  GROQ                       │
│              LLM Generation                 │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│             FINAL RESPONSE                  │
│        Answer + Document + Page             │
└──────────────────────────────────────────────┘
🎯 Project Goals

The project was designed around the following goals:

📚 Make research papers easier to explore
🔎 Reduce manual searching through long PDFs
🤖 Provide AI-assisted research interaction
🧠 Apply Retrieval-Augmented Generation concepts
🧩 Implement structured AI workflows with LangGraph
📑 Maintain document/page source awareness
☁️ Deploy an AI application to the cloud
🚀 Future Improvements

Potential future enhancements include:

🧠 Semantic embedding-based retrieval
🔢 Vector similarity search
🗄️ Persistent vector database
📚 Improved multi-document retrieval
🔗 More precise citation mapping
💬 Conversation memory
⚡ Streaming responses
📊 Retrieval evaluation
🔬 Advanced LangSmith tracing
🔐 User authentication
📈 Research analytics
🎓 What This Project Demonstrates

This project demonstrates practical experience with:

🐍 Python
⚡ FastAPI
🤖 Large Language Models
🧠 Retrieval-Augmented Generation
🔗 LangChain
🧩 LangGraph
📄 PDF Processing
✂️ Text Chunking
🔎 Information Retrieval
📝 Prompt Engineering
☁️ Cloud Deployment
🗄️ Cloud Storage
🔌 REST APIs

👩‍💻 Developer
<div align="center"> <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=8B5E3C&center=true&vCenter=true&width=650&lines=Developed+by+Hania+Eman;AI+%26+Data+Science+Student;ML+Developer+%7C+Python+Enthusiast" alt="Developer Animation" /> <br> <a href="https://github.com/haniaeman2026-pixel"> <img src="https://img.shields.io/badge/GitHub-Hania%20Eman-181717?style=for-the-badge&logo=github&logoColor=white" /> </a> </div>
<div align="center">
⭐ Research Paper Assistant
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=17&pause=1000&color=8B5E3C&center=true&vCenter=true&width=700&lines=Upload.+Retrieve.+Understand.;Built+with+Python+%7C+FastAPI+%7C+LangChain;Powered+by+LangGraph+%26+Groq;Designed+for+Research-Focused+AI+Workflows" alt="Footer Animation" />

<br><br>

Developed by Hania Eman

</div> ```
