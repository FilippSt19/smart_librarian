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

                {loading && (

                    <ChatMessage
                        role="assistant"
                        content="Finding the best match for you..."
                    />

                )}

                <div ref={bottomRef} />

            </div>

        </section>
    );
}