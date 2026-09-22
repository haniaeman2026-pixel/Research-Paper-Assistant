from typing import TypedDict, List

from langchain_core.documents import Document

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from app.llm import (
    generate_answer,
    UNAVAILABLE_MESSAGE,
)

from app.rag import (
    build_context,
    get_sources,
    retrieve_documents_with_scores,
)


# ---------------------------------------------------------
# Research State
# ---------------------------------------------------------

class ResearchState(TypedDict, total=False):

    question: str

    documents: List[Document]

    context: str

    sources: List[dict]

    answer: str

    has_relevant_context: bool


# ---------------------------------------------------------
# Retrieve Node
# ---------------------------------------------------------

def retrieve_node(
    state: ResearchState,
) -> ResearchState:

    question = state.get(
        "question",
        "",
    ).strip()

    if not question:

        return {
            "documents": [],
            "has_relevant_context": False,
        }

    results = (
        retrieve_documents_with_scores(
            question,
            k=5,
        )
    )

    documents = [
        document
        for document, score in results
    ]

    return {
        "documents": documents,
        "has_relevant_context": bool(
            documents
        ),
    }


# ---------------------------------------------------------
# Relevance Check
# ---------------------------------------------------------

def check_relevance_node(
    state: ResearchState,
) -> ResearchState:

    documents = state.get(
        "documents",
        [],
    )

    return {
        "has_relevant_context": bool(
            documents
        )
    }


# ---------------------------------------------------------
# Routing
# ---------------------------------------------------------

def route_after_relevance(
    state: ResearchState,
) -> str:

    if state.get(
        "has_relevant_context",
        False,
    ):

        return "prepare_context"

    return "unavailable"


# ---------------------------------------------------------
# Unavailable Node
# ---------------------------------------------------------

def unavailable_node(
    state: ResearchState,
) -> ResearchState:

    return {
        "answer": UNAVAILABLE_MESSAGE,
        "sources": [],
    }


# ---------------------------------------------------------
# Context Preparation
# ---------------------------------------------------------

def context_node(
    state: ResearchState,
) -> ResearchState:

    documents = state.get(
        "documents",
        [],
    )

    if not documents:

        return {
            "context": "",
            "sources": [],
        }

    context = build_context(
        documents
    )

    sources = get_sources(
        documents
    )

    return {
        "context": context,
        "sources": sources,
    }


# ---------------------------------------------------------
# Generate Answer
# ---------------------------------------------------------

def generate_node(
    state: ResearchState,
) -> ResearchState:

    question = state.get(
        "question",
        "",
    )

    context = state.get(
        "context",
        "",
    )

    if not context:

        return {
            "answer": UNAVAILABLE_MESSAGE
        }

    answer = generate_answer(
        question=question,
        context=context,
    )

    return {
        "answer": answer
    }


# ---------------------------------------------------------
# Build LangGraph
# ---------------------------------------------------------

def build_graph():

    graph = StateGraph(
        ResearchState
    )

    # Nodes
    graph.add_node(
        "retrieve",
        retrieve_node,
    )

    graph.add_node(
        "check_relevance",
        check_relevance_node,
    )

    graph.add_node(
        "prepare_context",
        context_node,
    )

    graph.add_node(
        "generate",
        generate_node,
    )

    graph.add_node(
        "unavailable",
        unavailable_node,
    )

    # ---------------------------------------------
    # Starting point
    # ---------------------------------------------

    graph.add_edge(
        START,
        "retrieve",
    )

    # ---------------------------------------------
    # Retrieval → Relevance
    # ---------------------------------------------

    graph.add_edge(
        "retrieve",
        "check_relevance",
    )

    # ---------------------------------------------
    # Relevance routing
    # ---------------------------------------------

    graph.add_conditional_edges(
        "check_relevance",
        route_after_relevance,
        {
            "prepare_context":
                "prepare_context",

            "unavailable":
                "unavailable",
        },
    )

    # ---------------------------------------------
    # Context → Generation
    # ---------------------------------------------

    graph.add_edge(
        "prepare_context",
        "generate",
    )

    # ---------------------------------------------
    # End points
    # ---------------------------------------------

    graph.add_edge(
        "generate",
        END,
    )

    graph.add_edge(
        "unavailable",
        END,
    )

    return graph.compile()


# ---------------------------------------------------------
# Compiled Research Graph
# ---------------------------------------------------------

research_graph = build_graph()


# ---------------------------------------------------------
# Public Question Function
# ---------------------------------------------------------

def ask_research_question(
    question: str,
) -> dict:

    question = question.strip()

    if not question:

        return {
            "answer": (
                "Please enter a question."
            ),
            "sources": [],
            "retrieved_chunks": 0,
        }

    result = research_graph.invoke(
        {
            "question": question
        }
    )

    return {
        "answer": result.get(
            "answer",
            UNAVAILABLE_MESSAGE,
        ),

        "sources": result.get(
            "sources",
            [],
        ),

        "retrieved_chunks": len(
            result.get(
                "documents",
                [],
            )
        ),
    }