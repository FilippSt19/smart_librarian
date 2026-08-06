import "../styles/chat.css";
import ReactMarkdown from "react-markdown";
import { FaRobot } from "react-icons/fa";

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

            {!isUser && (

                <div className="message-avatar assistant-avatar">

                    <FaRobot />

                </div>

            )}

            <div className="message-bubble">

                <div className="message-role">

                    {isUser
                        ? "You"
                        : "Smart Librarian"}

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