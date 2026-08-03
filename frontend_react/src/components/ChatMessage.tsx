import "../styles/chat.css";

type ChatMessageProps = {
    role: "user" | "assistant";
    content: string;
};

export default function ChatMessage({
    role,
    content,
}: ChatMessageProps) {

    const isUser = role === "user";

    return (
        <div
            className={
                isUser
                    ? "message message-user"
                    : "message message-assistant"
            }
        >
            <div className="message-bubble">

                <div className="message-role">

                    {isUser ? "🧑 You" : "📚 Assistant"}

                </div>

                <div className="message-content">

                    {content}

                </div>

            </div>
        </div>
    );
}