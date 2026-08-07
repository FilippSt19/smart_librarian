import ChatMessage from "./ChatMessage";

import type {
    ChatMessage as Message,
} from "../types/chat";

import { useAutoScroll } from "../hooks/useAutoScroll";


type Props = {
    messages: Message[];
    loading: boolean;
    onSend: (message: string) => void;
};


const SUGGESTIONS = [
    "Fantasy about friendship",
    "A classic romance",
    "A dystopian novel",
];


export default function ChatWindow({
    messages,
    loading,
    onSend,
}: Props) {

    const bottomRef = useAutoScroll(messages);

    const isEmptyState =
        messages.length === 1 &&
        messages[0].role === "assistant";

    return (
        <section className="chat-window">

            <div className="chat-window__content">

                {messages.map((message) => (

                    <ChatMessage
                        key={message.id}
                        role={message.role}
                        content={message.content}
                        recommendation={
                            message.recommendation
                        }
                    />

                ))}

                {isEmptyState && (

                    <div className="chat-empty-state">

                        <p className="chat-empty-state__label">
                            Try asking for
                        </p>

                        <div className="chat-empty-state__suggestions">

                            {SUGGESTIONS.map(
                                (suggestion) => (

                                    <button
                                        key={suggestion}
                                        type="button"
                                        className="chat-suggestion"
                                        onClick={() =>
                                            onSend(suggestion)
                                        }
                                        disabled={loading}
                                    >
                                        {suggestion}
                                    </button>

                                )
                            )}

                        </div>

                    </div>

                )}

                {loading && (

                    <div className="message message-assistant">

                        <div className="message-avatar assistant-avatar">
                            <span className="loading-robot">
                                AI
                            </span>
                        </div>

                        <div className="typing-indicator">

                            <span />
                            <span />
                            <span />

                        </div>

                    </div>

                )}

                <div ref={bottomRef} />

            </div>

        </section>
    );
}