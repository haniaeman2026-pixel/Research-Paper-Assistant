from pathlib import Path
from typing import List, Tuple

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.pdf_loader import load_pdf


# ---------------------------------------------------------
# In-memory document store
# ---------------------------------------------------------

DOCUMENT_STORE: List[Document] = []


# ---------------------------------------------------------
# Text splitter
# ---------------------------------------------------------

def split_documents(
    documents: List[Document],
) -> List[Document]:
    """
    Split extracted PDF pages into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    chunks = splitter.split_documents(
        documents
    )

    return chunks


# ---------------------------------------------------------
# Chunk IDs
# ---------------------------------------------------------

def create_chunk_ids(
    chunks: List[Document],
    filename: str,
) -> List[str]:
    """
    Create unique IDs for each document chunk.
    """

    ids = []

    for index, chunk in enumerate(chunks):

        page = chunk.metadata.get(
            "page",
            0,
        )

        chunk_id = (
            f"{filename}-"
            f"page-{page}-"
            f"chunk-{index}"
        )

        ids.append(chunk_id)

    return ids


# ---------------------------------------------------------
# Index PDF
# ---------------------------------------------------------

def index_pdf(
    pdf_path: Path,
) -> dict:
    """
    Extract PDF text, create chunks,
    attach metadata, and store chunks.
    """

    global DOCUMENT_STORE

    documents = load_pdf(
        pdf_path
    )

    if not documents:

        raise ValueError(
            "No readable text was found "
            "in this PDF."
        )

    chunks = split_documents(
        documents
    )

    if not chunks:

        raise ValueError(
            "Could not create text chunks."
        )

    filename = pdf_path.name

    ids = create_chunk_ids(
        chunks,
        filename,
    )

    # ---------------------------------------------
    # Add useful metadata to every chunk
    # ---------------------------------------------

    for index, chunk in enumerate(chunks):

        page = chunk.metadata.get(
            "page",
            0,
        )

        chunk.metadata["source"] = (
            filename
        )

        chunk.metadata["page"] = (
            page
        )

        chunk.metadata["chunk_id"] = (
            ids[index]
        )

    # ---------------------------------------------
    # Remove previous chunks belonging
    # to the same PDF
    # ---------------------------------------------

    DOCUMENT_STORE = [
        document
        for document in DOCUMENT_STORE
        if document.metadata.get(
            "source"
        ) != filename
    ]

    # ---------------------------------------------
    # Add new chunks
    # ---------------------------------------------

    DOCUMENT_STORE.extend(
        chunks
    )

    return {
        "filename": filename,
        "pages": len(documents),
        "chunks": len(chunks),
        "ids": ids,
    }


# ---------------------------------------------------------
# Simple lexical retrieval
# ---------------------------------------------------------

def retrieve_documents_with_scores(
    question: str,
    k: int = 5,
) -> List[Tuple[Document, float]]:
    """
    Retrieve relevant chunks using lightweight
    keyword-based scoring.

    This version avoids heavy embedding models,
    making it suitable for the current Vercel
    deployment architecture.
    """

    if not question.strip():

        return []

    if not DOCUMENT_STORE:

        return []

    # ---------------------------------------------
    # Normalize question
    # ---------------------------------------------

    question_words = {
        word.lower().strip(
            ".,!?;:()[]{}\"'"
        )
        for word in question.split()
        if len(word.strip()) > 2
    }

    if not question_words:

        return []

    scored_documents = []

    # ---------------------------------------------
    # Score every chunk
    # ---------------------------------------------

    for document in DOCUMENT_STORE:

        text = document.page_content.lower()

        score = 0.0

        # Individual keyword matches
        for word in question_words:

            if word in text:

                score += 1.0

        # -----------------------------------------
        # Extra score for exact phrase
        # -----------------------------------------

        question_lower = (
            question.lower().strip()
        )

        if question_lower in text:

            score += 5.0

        # -----------------------------------------
        # Only keep relevant chunks
        # -----------------------------------------

        if score > 0:

            scored_documents.append(
                (
                    document,
                    score,
                )
            )

    # ---------------------------------------------
    # Highest score first
    # ---------------------------------------------

    scored_documents.sort(
        key=lambda item: item[1],
        reverse=True,
    )

    return scored_documents[:k]


# ---------------------------------------------------------
# Retrieve documents
# ---------------------------------------------------------

def retrieve_documents(
    question: str,
    k: int = 5,
) -> List[Document]:
    """
    Return retrieved documents.
    """

    results = retrieve_documents_with_scores(
        question,
        k=k,
    )

    return [
        document
        for document, score in results
    ]


# ---------------------------------------------------------
# Build LLM context
# ---------------------------------------------------------

def build_context(
    documents: List[Document],
) -> str:
    """
    Build the context sent to the LLM.
    """

    if not documents:

        return ""

    context_parts = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown document",
        )

        page = document.metadata.get(
            "page",
            "Unknown",
        )

        context_parts.append(
            f"""
SOURCE: {source}
PAGE: {page}

CONTENT:
{document.page_content}
"""
        )

    return (
        "\n\n"
        "-------------------------"
        "\n\n"
    ).join(
        context_parts
    )


# ---------------------------------------------------------
# Sources
# ---------------------------------------------------------

def get_sources(
    documents: List[Document],
) -> List[dict]:
    """
    Return unique document/page sources.
    """

    sources = []

    seen = set()

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown document",
        )

        page = document.metadata.get(
            "page",
        )

        key = (
            source,
            page,
        )

        if key in seen:

            continue

        seen.add(
            key
        )

        sources.append(
            {
                "document": source,
                "page": page,
            }
        )

    return sources