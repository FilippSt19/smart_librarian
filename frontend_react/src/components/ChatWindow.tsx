import ChatMessage from "./ChatMessage";

import type {
    ChatMessage as Message,
} from "../types/chat";

import { useAutoScroll } from "../hooks/useAutoScroll";

type Props = {
    messages: Message[];
    loading: boolean;
};

export default function ChatWindow({
    messages,
    loading,
}: Props) {

    const bottomRef = useAutoScroll(messages);

    return (
        <div className="chat-window">

            {messages.map((message) => (

                <ChatMessage
                    key={message.id}
                    role={message.role}
                    content={message.content}
                />

            ))}

            {loading && (

                <ChatMessage
                    role="assistant"
                    content="⏳ Thinking..."
                />

            )}

            <div ref={bottomRef} />

        </div>
    );
}