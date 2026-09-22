import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")
load_dotenv(BASE_DIR / ".env.local")


GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY",
    "",
)

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-20b",
)


LANGSMITH_TRACING = os.getenv(
    "LANGSMITH_TRACING",
    "false",
).lower() == "true"

LANGSMITH_API_KEY = os.getenv(
    "LANGSMITH_API_KEY",
    "",
)

LANGSMITH_PROJECT = os.getenv(
    "LANGSMITH_PROJECT",
    "research-paper-assistant",
)


UPLOAD_DIR = BASE_DIR / "uploads"

CHROMA_DIR = BASE_DIR / "chroma_db"


UPLOAD_DIR.mkdir(
    exist_ok=True
)

CHROMA_DIR.mkdir(
    exist_ok=True
)