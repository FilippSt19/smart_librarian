import { useState } from "react";

import Navbar from "./shared/navbar";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";
import { sendMessage } from "./services/api";

import type {
    ChatMessage,
} from "./types/chat";

function App() {

    const [messages, setMessages] =
        useState<ChatMessage[]>([
            {
                id: crypto.randomUUID(),
                role: "assistant",
                content:
                    "Hello! 👋\n\nTell me what kind of book you are looking for.",
            },
        ]);

    async function handleSend(
        message: string
    ) {

        // User message

        const userMessage = {
            id: crypto.randomUUID(),
            role: "user" as const,
            content: message,
        };

        setMessages((previous) => [

            ...previous,

            userMessage,

        ]);

        try {

            const result = await sendMessage(message);

            const assistantMessage = {

                id: crypto.randomUUID(),

                role: "assistant" as const,

                content: result.response,

            };

            setMessages((previous) => [

                ...previous,

                assistantMessage,

            ]);

        } catch (error) {

            const assistantMessage = {

                id: crypto.randomUUID(),

                role: "assistant" as const,

                content:
                    "❌ Unable to contact the backend.",

            };

            setMessages((previous) => [

                ...previous,

                assistantMessage,

            ]);

            console.error(error);

        }

    }

    return (
        <>

            <Navbar />

            <Header
                title=" Smart Librarian"
                subtitle="Discover your next favorite book using AI."
            />

            <ChatWindow
                messages={messages}
            />

            <ChatInput
                onSend={handleSend}
            />

        </>
    );
}

export default App;