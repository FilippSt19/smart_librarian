import "../styles/chat.css";
import ReactMarkdown from "react-markdown";

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

                    <ReactMarkdown>
                        {content}
                    </ReactMarkdown>

                </div>

            </div>
        </div>
    );
}