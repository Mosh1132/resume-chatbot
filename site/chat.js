const API_URL = location.hostname === "localhost"
    ? "http://127.0.0.1:8080"
    : "https://resume-chatbot-612795367728.us-central1.run.app";
const sessionId = crypto.randomUUID();
const messages = document.getElementById("messages");
const form = document.getElementById("chat-form");
const input = document.getElementById("chat-input");
const sendButton = document.getElementById("send");

function addBubble(role, text){
    const bubble = document.createElement("div");
    bubble.className = `bubble ${role}`;
    bubble.textContent = text;
    messages.appendChild(bubble);
    messages.scrollTop = messages.scrollHeight;
    return bubble;
};

addBubble("bot", "Hi, ask me anything about my experience");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const question = input.value.trim();
    if (question === "") {
        return;
    }

    addBubble("user", question);
    input.value = "";
    input.disabled = true;
    sendButton.disabled = true;

    const bubble = addBubble("bot", "");

    try {
        const response = await fetch(`${API_URL}/chat/stream`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ session_id: sessionId, question: question }),
        });

        if (response.status === 429) {
            throw new Error("rate limited");
        }
        if (!response.ok) {
            throw new Error(`Server replied ${response.status}`);
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        bubble.textContent = "";

        while (true) {
            const { done, value } = await reader.read();
            if (done) {
                break;
            }
            bubble.textContent += decoder.decode(value, { stream: true });
            messages.scrollTop = messages.scrollHeight;
        }
    } catch (error) {
        if (error.message === "rate limited") {
            bubble.textContent = "You're asking quickly. Please wait a minute and try again.";
        } else {
            bubble.textContent = "Sorry, something went wrong. Please try again.";
        }
    } finally {
        input.disabled = false;
        sendButton.disabled = false;
        input.focus();
    }
});