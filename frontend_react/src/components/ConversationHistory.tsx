import {
    FaClockRotateLeft,
    FaPlus,
    FaTrash,
} from "react-icons/fa6";

import type {
    Conversation,
} from "../types/chat";

import "../styles/history.css";


type ConversationHistoryProps = {
    conversations: Conversation[];
    activeConversationId: string;
    onNewConversation: () => void;
    onSelectConversation: (conversationId: string) => void;
    onDeleteConversation: (conversationId: string) => void;
};


export default function ConversationHistory({
    conversations,
    activeConversationId,
    onNewConversation,
    onSelectConversation,
    onDeleteConversation,
}: ConversationHistoryProps) {

    return (
        <aside className="history">

            <button
                className="history__new"
                type="button"
                onClick={onNewConversation}
            >
                <FaPlus />

                <span>New chat</span>
            </button>

            <div className="history__heading">

                <FaClockRotateLeft />

                <span>History</span>

            </div>

            <div className="history__list">

                {conversations.map((conversation) => {

                    const isActive =
                        conversation.id === activeConversationId;

                    return (
                        <div
                            key={conversation.id}
                            className={
                                isActive
                                    ? "history__item history__item--active"
                                    : "history__item"
                            }
                        >
                            <button
                                className="history__conversation"
                                type="button"
                                onClick={() =>
                                    onSelectConversation(
                                        conversation.id,
                                    )
                                }
                            >
                                <span className="history__title">
                                    {conversation.title}
                                </span>
                            </button>

                            <button
                                className="history__delete"
                                type="button"
                                aria-label={`Delete ${conversation.title}`}
                                title="Delete conversation"
                                onClick={() =>
                                    onDeleteConversation(
                                        conversation.id,
                                    )
                                }
                            >
                                <FaTrash />
                            </button>
                        </div>
                    );
                })}

            </div>

        </aside>
    );
}