from groq import Groq

from app.config import (
    GROQ_API_KEY,
    GROQ_MODEL,
)


_client = None


UNAVAILABLE_MESSAGE = (
    "The answer is not available "
    "in the uploaded research papers."
)


def get_groq_client():

    global _client

    if _client is None:

        if not GROQ_API_KEY:

            raise ValueError(
                "GROQ_API_KEY is not configured "
                "in the .env file."
            )

        _client = Groq(
            api_key=GROQ_API_KEY
        )

    return _client


def generate_answer(
    question: str,
    context: str,
) -> str:

    client = get_groq_client()

    if not context.strip():

        return UNAVAILABLE_MESSAGE


    system_prompt = f"""
You are a Research Paper Assistant.

Your task is to answer the user's question using ONLY the
RESEARCH PAPER CONTEXT provided below.

IMPORTANT RULES:

1. Use only information present in the provided context.

2. Do not use outside knowledge.

3. Do not guess or invent information.

4. If the context contains information that answers the
   question, give the answer clearly and directly.

5. If the context does NOT contain enough information to
   answer the question, respond exactly:

"{UNAVAILABLE_MESSAGE}"

6. When possible, mention the relevant source information
   already provided in the context.

7. For questions about the paper's problem, methodology,
   architecture, dataset, experiments, findings, limitations,
   or future work, summarize only what is supported by the
   retrieved context.

8. Do not refuse an answer merely because the exact wording
   of the question is not present. Look for the meaning of
   the question in the provided context.

9. Never use information outside the retrieved research paper
   context.

"""

    user_prompt = f"""
RESEARCH PAPER CONTEXT
======================

{context}

======================

USER QUESTION
=============

{question}

======================

Answer using ONLY the research paper context above.
"""


    response = client.chat.completions.create(
        model=GROQ_MODEL,

        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },

            {
                "role": "user",
                "content": user_prompt,
            },
        ],

        temperature=0,

        max_tokens=1000,
    )


    answer = (
        response
        .choices[0]
        .message
        .content
    )


    if not answer:

        return UNAVAILABLE_MESSAGE


    return answer.strip()