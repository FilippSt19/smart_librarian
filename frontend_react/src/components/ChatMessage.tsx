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
            style={{
                display: "flex",
                justifyContent: isUser
                    ? "flex-end"
                    : "flex-start",
                marginBottom: "16px",
            }}
        >
            <div
                style={{
                    maxWidth: "70%",
                    padding: "14px",
                    borderRadius: "12px",
                    backgroundColor: isUser
                        ? "#2563eb"
                        : "#ffffff",
                    color: isUser
                        ? "white"
                        : "#111827",
                    boxShadow:
                        "0 2px 6px rgba(0,0,0,0.1)",
                    whiteSpace: "pre-wrap",
                }}
            >
                {content}
            </div>
        </div>
    );
}