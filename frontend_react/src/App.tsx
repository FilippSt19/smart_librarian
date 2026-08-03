import { useState } from "react";

import Navbar from "./shared/navbar";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

import { sendMessage } from "./services/api";

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
        <>

            <Navbar />

            <Header
                title="📚 Smart Librarian"
                subtitle="Discover your next favorite book using AI."
            />

            <ChatWindow
                messages={messages}
                loading={loading}
            />

            <ChatInput
                onSend={handleSend}
            />

        </>
    );
}

export default App;