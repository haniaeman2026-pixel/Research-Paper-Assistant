from pathlib import Path
from typing import List

import pdfplumber
from pypdf import PdfReader

from langchain_core.documents import Document


def extract_with_pypdf(
    pdf_path: Path,
) -> List[Document]:

    documents = []

    reader = PdfReader(
        str(pdf_path)
    )

    for page_number, page in enumerate(
        reader.pages,
        start=1,
    ):

        text = page.extract_text() or ""

        text = text.strip()

        if not text:
            continue

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": pdf_path.name,
                    "page": page_number,
                    "loader": "PyPDF",
                },
            )
        )

    return documents


def extract_with_pdfplumber(
    pdf_path: Path,
) -> List[Document]:

    documents = []

    with pdfplumber.open(
        str(pdf_path)
    ) as pdf:

        for page_number, page in enumerate(
            pdf.pages,
            start=1,
        ):

            text = page.extract_text() or ""

            text = text.strip()

            if not text:
                continue

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": pdf_path.name,
                        "page": page_number,
                        "loader": "PDFPlumber",
                    },
                )
            )

    return documents


def load_pdf(
    pdf_path: Path,
) -> List[Document]:

    if not pdf_path.exists():

        raise FileNotFoundError(
            f"PDF file not found: {pdf_path}"
        )

    if pdf_path.suffix.lower() != ".pdf":

        raise ValueError(
            "Only PDF files are supported."
        )

    documents = extract_with_pypdf(
        pdf_path
    )

    if documents:
        return documents

    documents = extract_with_pdfplumber(
        pdf_path
    )

    if documents:
        return documents

    raise ValueError(
        "No readable text was found in this PDF. "
        "The PDF may contain scanned images only."
    )


def get_pdf_info(
    pdf_path: Path,
) -> dict:

    reader = PdfReader(
        str(pdf_path)
    )

    return {
        "filename": pdf_path.name,
        "pages": len(reader.pages),
    }