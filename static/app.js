const fileInput = document.getElementById("fileInput");
const fileList = document.getElementById("fileList");
const uploadBtn = document.getElementById("uploadBtn");
const uploadStatus = document.getElementById("uploadStatus");

const questionInput = document.getElementById("questionInput");
const askBtn = document.getElementById("askBtn");
const chatMessages = document.getElementById("chatMessages");
const clearChatBtn = document.getElementById("clearChatBtn");
const dropZone = document.getElementById("dropZone");

let selectedFiles = [];


/* ================================= */
/* FILE SELECTION */
/* ================================= */

fileInput.addEventListener("change", () => {

    selectedFiles = [...fileInput.files];

    renderFiles();

});


/* ================================= */
/* DRAG & DROP */
/* ================================= */

dropZone.addEventListener("dragover", (event) => {

    event.preventDefault();

    dropZone.classList.add("dragover");

});


dropZone.addEventListener("dragleave", () => {

    dropZone.classList.remove("dragover");

});


dropZone.addEventListener("drop", (event) => {

    event.preventDefault();

    dropZone.classList.remove("dragover");

    const files = [...event.dataTransfer.files];

    selectedFiles = files.filter(file =>
        file.name.toLowerCase().endsWith(".pdf")
    );

    renderFiles();

});


/* ================================= */
/* RENDER FILES */
/* ================================= */

function renderFiles() {

    fileList.innerHTML = "";

    if (!selectedFiles.length) {
        return;
    }

    selectedFiles.forEach((file) => {

        const item = document.createElement("div");

        item.className = "file-item";

        item.textContent = file.name;

        fileList.appendChild(item);

    });

}


/* ================================= */
/* UPLOAD */
/* ================================= */

uploadBtn.addEventListener("click", async () => {

    if (!selectedFiles.length) {

        showStatus(
            "Please select at least one PDF file.",
            "error"
        );

        return;
    }


    const invalidFile = selectedFiles.find(
        file =>
            !file.name
                .toLowerCase()
                .endsWith(".pdf")
    );


    if (invalidFile) {

        showStatus(
            `${invalidFile.name} is not a PDF file.`,
            "error"
        );

        return;
    }


    const formData = new FormData();


    selectedFiles.forEach(file => {

        formData.append(
            "files",
            file
        );

    });


    uploadBtn.disabled = true;

    uploadBtn.innerHTML =
        `<span class="btn-icon">◌</span> Processing papers...`;

    showStatus(
        "Extracting text, creating chunks and indexing your papers...",
        ""
    );


    try {

        const response = await fetch(
            "/api/upload",
            {
                method: "POST",
                body: formData
            }
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Upload failed."
            );

        }


        const summary = data.documents
            .map(
                doc =>
                    `${doc.filename} — ${doc.pages} pages · ${doc.chunks} chunks`
            )
            .join("\n");


        showStatus(
            `✓ Papers indexed successfully.\n${summary}`,
            "success"
        );


        addMessage(
            "assistant",
            "Your research papers are indexed and ready. Ask me anything about their content."
        );


    } catch (error) {

        showStatus(
            error.message,
            "error"
        );

    } finally {

        uploadBtn.disabled = false;

        uploadBtn.innerHTML =
            `<span class="btn-icon">✦</span> Index Research Papers`;

    }

});


/* ================================= */
/* ASK QUESTION */
/* ================================= */

askBtn.addEventListener(
    "click",
    askQuestion
);


questionInput.addEventListener(
    "keydown",
    event => {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            askQuestion();

        }

    }
);


/* ================================= */
/* AUTO RESIZE TEXTAREA */
/* ================================= */

questionInput.addEventListener(
    "input",
    () => {

        questionInput.style.height = "auto";

        questionInput.style.height =
            Math.min(
                questionInput.scrollHeight,
                120
            ) + "px";

    }
);


/* ================================= */
/* SUGGESTION BUTTONS */
/* ================================= */

document.querySelectorAll(
    ".suggestion"
).forEach(button => {

    button.addEventListener(
        "click",
        () => {

            questionInput.value =
                button.dataset.question;

            questionInput.dispatchEvent(
                new Event("input")
            );

            questionInput.focus();

        }
    );

});


/* ================================= */
/* ASK FUNCTION */
/* ================================= */

async function askQuestion() {

    const question =
        questionInput.value.trim();


    if (!question) {

        addMessage(
            "assistant",
            "Please enter a question first."
        );

        return;

    }


    addMessage(
        "user",
        question
    );


    questionInput.value = "";

    questionInput.style.height = "auto";

    askBtn.disabled = true;


    const thinking =
        addThinkingMessage();


    try {

        const response = await fetch(
            "/api/ask",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    question: question
                })
            }
        );


        const data =
            await response.json();


        thinking.remove();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Could not answer the question."
            );

        }


        addMessage(
            "assistant",
            data.answer,
            data.sources || []
        );


    } catch (error) {

        thinking.remove();


        addMessage(
            "assistant",
            `Error: ${error.message}`
        );


    } finally {

        askBtn.disabled = false;

        questionInput.focus();

    }

}


/* ================================= */
/* ADD MESSAGE */
/* ================================= */

function addMessage(
    role,
    text,
    sources = []
) {

    const wrapper =
        document.createElement("div");

    wrapper.className =
        `message ${role}`;


    const avatar =
        document.createElement("div");

    avatar.className =
        "avatar";

    avatar.textContent =
        role === "user"
            ? "YOU"
            : "AI";


    const content =
        document.createElement("div");

    content.className =
        "message-content";


    const paragraph =
        document.createElement("p");

    paragraph.textContent =
        text;


    content.appendChild(
        paragraph
    );


    /* SOURCES */

    if (
        role === "assistant" &&
        sources.length
    ) {

        const sourceBox =
            document.createElement("div");

        sourceBox.className =
            "sources";


        const title =
            document.createElement("div");

        title.className =
            "source-title";

        title.textContent =
            "Sources";


        sourceBox.appendChild(
            title
        );


        sources.forEach(
            source => {

                const item =
                    document.createElement("div");

                item.className =
                    "source-item";

                item.textContent =
                    `${source.document} — Page ${source.page}`;

                sourceBox.appendChild(
                    item
                );

            }
        );


        content.appendChild(
            sourceBox
        );

    }


    wrapper.appendChild(
        avatar
    );

    wrapper.appendChild(
        content
    );


    chatMessages.appendChild(
        wrapper
    );


    scrollChat();


    return wrapper;

}


/* ================================= */
/* THINKING MESSAGE */
/* ================================= */

function addThinkingMessage() {

    const wrapper =
        document.createElement("div");

    wrapper.className =
        "message assistant";


    const avatar =
        document.createElement("div");

    avatar.className =
        "avatar";

    avatar.textContent =
        "AI";


    const content =
        document.createElement("div");

    content.className =
        "message-content";


    const typing =
        document.createElement("div");

    typing.className =
        "typing";


    typing.innerHTML = `
        <span></span>
        <span></span>
        <span></span>
    `;


    content.appendChild(
        typing
    );


    wrapper.appendChild(
        avatar
    );

    wrapper.appendChild(
        content
    );


    chatMessages.appendChild(
        wrapper
    );


    scrollChat();


    return wrapper;

}


/* ================================= */
/* SCROLL CHAT */
/* ================================= */

function scrollChat() {

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


/* ================================= */
/* STATUS */
/* ================================= */

function showStatus(
    message,
    type
) {

    uploadStatus.textContent =
        message;

    uploadStatus.className =
        `status ${type}`;

}
// =========================================================
// CLEAR CHAT
// =========================================================

if (clearChatBtn) {
    clearChatBtn.addEventListener("click", () => {

        chatMessages.innerHTML = `
            <div class="welcome-message">

                <div class="welcome-icon">
                    ✦
                </div>

                <h4>Your papers are ready to talk.</h4>

                <p>
                    Upload a research paper and ask a question.
                    Answers are generated only from your uploaded documents.
                </p>

                <div class="suggestions">

                    <button
                        type="button"
                        class="suggestion-btn"
                        data-question="Summarize this research paper."
                    >
                        <span>Summary</span>
                        <span>→</span>
                    </button>

                    <button
                        type="button"
                        class="suggestion-btn"
                        data-question="What methodology or architecture does the paper propose?"
                    >
                        <span>Methodology</span>
                        <span>→</span>
                    </button>

                    <button
                        type="button"
                        class="suggestion-btn"
                        data-question="What are the key findings of this research paper?"
                    >
                        <span>Key findings</span>
                        <span>→</span>
                    </button>

                </div>

            </div>
        `;

        if (questionInput) {
            questionInput.value = "";
            questionInput.style.height = "auto";
            questionInput.focus();
        }

        attachSuggestionListeners();
    });
}


// =========================================================
// SUGGESTION BUTTONS
// =========================================================

function attachSuggestionListeners() {

    const suggestionButtons =
        document.querySelectorAll(".suggestion-btn");

    suggestionButtons.forEach(button => {

        button.addEventListener("click", () => {

            const question =
                button.dataset.question;

            if (!questionInput) {
                return;
            }

            questionInput.value = question;

            questionInput.dispatchEvent(
                new Event("input")
            );

            questionInput.focus();
        });

    });
}


attachSuggestionListeners();


// =========================================================
// ENTER TO ASK
// =========================================================

if (questionInput) {

    questionInput.addEventListener("keydown", (event) => {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            const askBtn =
                document.getElementById("askBtn");

            if (askBtn) {
                askBtn.click();
            }

        }

    });

}