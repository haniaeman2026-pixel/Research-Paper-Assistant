from pathlib import Path
import tempfile

from fastapi import (
    FastAPI,
    File,
    HTTPException,
    UploadFile,
)

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.models import QuestionRequest
from app.rag import index_pdf
from app.graph import ask_research_question
from app.blob_storage import upload_pdf_to_blob


BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)


app = FastAPI(
    title="Research Paper Assistant",
    version="1.0.0",
    description=(
        "RAG-based research paper assistant "
        "using LangChain, LangGraph, Groq "
        "and Vercel Blob."
    ),
)


app.mount(
    "/static",
    StaticFiles(
        directory=BASE_DIR / "static"
    ),
    name="static",
)


@app.get(
    "/",
    response_class=HTMLResponse,
)
async def home():

    index_file = (
        BASE_DIR
        / "templates"
        / "index.html"
    )

    if not index_file.exists():

        raise HTTPException(
            status_code=500,
            detail="Frontend file not found.",
        )

    return index_file.read_text(
        encoding="utf-8"
    )


@app.get("/api/health")
async def health():

    return {
        "status": "online",
        "service": "Research Paper Assistant",
        "version": "1.0.0",
        "storage": "Vercel Blob",
    }


@app.post("/api/upload")
async def upload_papers(
    files: list[UploadFile] = File(...),
):

    if not files:

        raise HTTPException(
            status_code=400,
            detail=(
                "Please upload at least "
                "one PDF file."
            ),
        )


    results = []


    for file in files:

        if not file.filename:
            continue


        filename = Path(
            file.filename
        ).name


        if not filename.lower().endswith(
            ".pdf"
        ):

            raise HTTPException(
                status_code=400,
                detail=(
                    f"Unsupported file format: "
                    f"{filename}. "
                    "Please upload PDF files only."
                ),
            )


        content = await file.read()


        if not content:

            raise HTTPException(
                status_code=400,
                detail=(
                    f"The uploaded file is empty: "
                    f"{filename}"
                ),
            )


        # ---------------------------------
        # Temporary local file for indexing
        # ---------------------------------

        temp_path = (
            Path(tempfile.gettempdir())
            / filename
        )


        temp_path.write_bytes(
            content
        )


        try:

            # -----------------------------
            # Extract and chunk PDF
            # -----------------------------

            result = index_pdf(
                temp_path
            )


            # -----------------------------
            # Store original PDF in Blob
            # -----------------------------

            blob_result = upload_pdf_to_blob(
                filename=filename,
                content=content,
            )


        except Exception as exc:

            if temp_path.exists():
                temp_path.unlink()

            raise HTTPException(
                status_code=400,
                detail=(
                    f"Could not process "
                    f"{filename}: {exc}"
                ),
            )


        finally:

            if temp_path.exists():
                temp_path.unlink()


        results.append(
            {
                "filename":
                    result["filename"],

                "pages":
                    result["pages"],

                "chunks":
                    result["chunks"],

                "blob_path":
                    blob_result["pathname"],

                "status":
                    "indexed",
            }
        )


    if not results:

        raise HTTPException(
            status_code=400,
            detail=(
                "No valid PDF files "
                "were uploaded."
            ),
        )


    return {

        "message": (
            "Research papers uploaded "
            "and indexed successfully."
        ),

        "documents": results,
    }


@app.post("/api/ask")
async def ask_question(
    request: QuestionRequest,
):

    question = request.question.strip()


    if not question:

        raise HTTPException(
            status_code=400,
            detail="Please enter a question.",
        )


    try:

        result = ask_research_question(
            question
        )


    except ValueError as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=(
                "Could not generate an answer: "
                f"{exc}"
            ),
        )


    return result