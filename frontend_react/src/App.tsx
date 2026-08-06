import { useState } from "react";

import Navbar from "./shared/navbar";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

import { sendMessage } from "./services/api";
import "./styles/app.css";

import type { ChatMessage } from "./types/chat";

function App() {

    const [messages, setMessages] = useState<ChatMessage[]>([
        {
            id: crypto.randomUUID(),
            role: "assistant",
            content:
                "Hello! 👋\n\nTell me what kind of book you are looking for.",
        },
    ]);

    const [loading, setLoading] = useState(false);

    async function handleSend(
        message: string
    ) {

        const userMessage: ChatMessage = {
            id: crypto.randomUUID(),
            role: "user",
            content: message,
        };

        setMessages((previous) => [
            ...previous,
            userMessage,
        ]);

        setLoading(true);

        try {

            const result = await sendMessage(message);

            const assistantMessage: ChatMessage = {
                id: crypto.randomUUID(),
                role: "assistant",
                content: result.response,
            };

            setMessages((previous) => [
                ...previous,
                assistantMessage,
            ]);

        } catch (error) {

            console.error(error);

            const errorMessage: ChatMessage = {
                id: crypto.randomUUID(),
                role: "assistant",
                content:
                    "❌ Sorry, something went wrong while contacting the backend.",
            };

            setMessages((previous) => [
                ...previous,
                errorMessage,
            ]);

        } finally {

            setLoading(false);

        }

    }

    return (
        <div className="app-shell">
            <Navbar />

            <main className="main-content">
                <div className="content-wrapper">
                    <Header
                        title="What would you like to read today?"
                        subtitle="Describe your favorite genres, authors or themes and I'll recommend the perfect book."
                    />

                    <section className="chat-section">
                        <div className="chat-card">

                            <ChatWindow
                                messages={messages}
                                loading={loading}
                            />

                            <div className="chat-card__footer">

                                <ChatInput
                                    onSend={handleSend}
                                />

                            </div>

                        </div>
                    </section>
                </div>
            </main>
        </div>
    );
}

export default App;