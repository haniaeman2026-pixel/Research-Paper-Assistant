import os
import tempfile
from pathlib import Path

from vercel import blob


BLOB_ACCESS = "private"


def upload_pdf_to_blob(
    filename: str,
    content: bytes,
) -> dict:
    """
    Upload a PDF to Vercel Blob.

    The PDF is temporarily written to /tmp because
    Vercel's deployed filesystem is read-only.
    """

    safe_filename = Path(filename).name

    temp_path = (
        Path(tempfile.gettempdir())
        / safe_filename
    )

    temp_path.write_bytes(content)

    try:
        uploaded = blob.upload_file(
    local_path=str(temp_path),
    path=f"research-papers/{safe_filename}",
    access=BLOB_ACCESS,
    allow_overwrite=True,
)

        return {
            "pathname": getattr(
                uploaded,
                "pathname",
                f"research-papers/{safe_filename}",
            ),
            "url": getattr(
                uploaded,
                "url",
                None,
            ),
        }

    finally:

        if temp_path.exists():
            temp_path.unlink()