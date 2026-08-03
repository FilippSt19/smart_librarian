import ChatMessage from "./ChatMessage";

import type {
    ChatMessage as Message,
} from "../types/chat";

type Props = {
    messages: Message[];
};

export default function ChatWindow({
    messages,
}: Props) {

    return (
        <div className="chat-window">

            {messages.map((message) => (

                <ChatMessage
                    key={message.id}
                    role={message.role}
                    content={message.content}
                />

            ))}

        </div>
    );
}