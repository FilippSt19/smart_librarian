import ReactMarkdown from "react-markdown";
import { FaRobot } from "react-icons/fa";

import BookRecommendationCard from "./BookRecommendationCard";

import type {
    BookRecommendation,
} from "../types/chat";

import "../styles/chat.css";


type ChatMessageProps = {
    role: "user" | "assistant";
    content?: string;
    recommendation?: BookRecommendation;
};


export default function ChatMessage({
    role,
    content,
    recommendation,
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

            <div
                className={
                    recommendation
                        ? "message-body message-body--recommendation"
                        : "message-bubble"
                }
            >

                {!isUser && !recommendation && (

                    <div className="message-role">
                        Smart Librarian
                    </div>

                )}

                {content && (

                    <div className="message-content">
                        <ReactMarkdown>
                            {content}
                        </ReactMarkdown>
                    </div>

                )}

                {recommendation && (

                    <BookRecommendationCard
                        recommendation={recommendation}
                    />

                )}

            </div>

        </div>
    );
}