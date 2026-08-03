import ChatMessage from "./ChatMessage";

export type Message = {
    role: "user" | "assistant";
    content: string;
};

type ChatWindowProps = {
    messages: Message[];
};

export default function ChatWindow({
    messages,
}: ChatWindowProps) {

    return (
        <div
            style={{
                padding: "24px",
                display: "flex",
                flexDirection: "column",
                gap: "16px",
                overflowY: "auto",
            }}
        >
            {messages.map((message, index) => (
                <ChatMessage
                    key={index}
                    role={message.role}
                    content={message.content}
                />
            ))}
        </div>
    );
}