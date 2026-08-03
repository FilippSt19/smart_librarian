import { useState } from "react";

import Navbar from "./shared/navbar";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

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

    function handleSend(
        message: string
    ) {

        setMessages((previous) => [

            ...previous,

            {
                id: crypto.randomUUID(),
                role: "user",
                content: message,
            },

        ]);
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
            />

            <ChatInput
                onSend={handleSend}
            />

        </>
    );
}

export default App;