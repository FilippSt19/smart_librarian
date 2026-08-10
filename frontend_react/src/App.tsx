import {
    useEffect,
    useState,
} from "react";

import Navbar from "./shared/navbar";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";
import ConversationHistory from "./components/ConversationHistory";

import { sendMessage } from "./services/api";

import type {
    ChatMessage,
    Conversation,
} from "./types/chat";

import "./styles/app.css";


const STORAGE_KEY = "smart-librarian-conversations";

const DEFAULT_CONVERSATION_TITLE = "New conversation";

const WELCOME_MESSAGE =
    "Hello! Tell me what kind of book you are looking for.";


function createConversation(): Conversation {

    const now = new Date().toISOString();

    return {
        id: crypto.randomUUID(),
        title: DEFAULT_CONVERSATION_TITLE,
        createdAt: now,
        updatedAt: now,
        messages: [
            {
                id: crypto.randomUUID(),
                role: "assistant",
                content: WELCOME_MESSAGE,
            },
        ],
    };
}


function hasUserMessages(
    conversation: Conversation,
): boolean {

    return conversation.messages.some(
        (message) =>
            message.role === "user",
    );
}


function createConversationTitle(
    message: string,
): string {

    const normalizedMessage =
        message.trim().replace(/\s+/g, " ");

    if (normalizedMessage.length <= 32) {
        return normalizedMessage;
    }

    return `${normalizedMessage.slice(0, 32).trim()}...`;
}


function loadConversations(): Conversation[] {

    try {

        const storedConversations =
            localStorage.getItem(STORAGE_KEY);

        if (!storedConversations) {
            return [createConversation()];
        }

        const parsedConversations =
            JSON.parse(storedConversations) as Conversation[];

        if (
            !Array.isArray(parsedConversations) ||
            parsedConversations.length === 0
        ) {
            return [createConversation()];
        }

        const meaningfulConversations =
            parsedConversations.filter(
                hasUserMessages,
            );

        if (meaningfulConversations.length === 0) {
            return [createConversation()];
        }

        return meaningfulConversations;

    } catch (error) {

        console.error(
            "Could not load conversation history.",
            error,
        );

        return [createConversation()];
    }
}


function App() {

    const [conversations, setConversations] =
        useState<Conversation[]>(loadConversations);

    const [activeConversationId, setActiveConversationId] =
        useState<string>(() => conversations[0].id);

    const [loading, setLoading] =
        useState(false);


    const activeConversation =
        conversations.find(
            (conversation) =>
                conversation.id === activeConversationId,
        ) ?? conversations[0];


    useEffect(() => {

        const conversationsToStore =
            conversations.filter(
                hasUserMessages,
            );

        localStorage.setItem(
            STORAGE_KEY,
            JSON.stringify(
                conversationsToStore,
            ),
        );

    }, [conversations]);


    function updateConversation(
        conversationId: string,
        updater: (conversation: Conversation) => Conversation,
    ) {

        setConversations((previous) =>
            previous.map((conversation) =>
                conversation.id === conversationId
                    ? updater(conversation)
                    : conversation,
            ),
        );
    }


    function handleNewConversation() {

        if (
            activeConversation &&
            !hasUserMessages(
                activeConversation,
            )
        ) {
            return;
        }

        const conversation =
            createConversation();

        setConversations((previous) => [
            conversation,
            ...previous,
        ]);

        setActiveConversationId(
            conversation.id,
        );

        setLoading(false);
    }


    function handleSelectConversation(
        conversationId: string,
    ) {

        if (loading) {
            return;
        }

        setActiveConversationId(
            conversationId,
        );
    }


    function handleDeleteConversation(
        conversationId: string,
    ) {

        if (loading) {
            return;
        }

        setConversations((previous) => {

            const remainingConversations =
                previous.filter(
                    (conversation) =>
                        conversation.id !== conversationId,
                );

            if (remainingConversations.length === 0) {

                const newConversation =
                    createConversation();

                setActiveConversationId(
                    newConversation.id,
                );

                return [newConversation];
            }

            if (
                conversationId === activeConversationId
            ) {
                setActiveConversationId(
                    remainingConversations[0].id,
                );
            }

            return remainingConversations;
        });
    }


    async function handleSend(
        message: string,
    ) {

        if (!activeConversation || loading) {
            return;
        }

        const conversationId =
            activeConversation.id;

        const userMessage: ChatMessage = {
            id: crypto.randomUUID(),
            role: "user",
            content: message,
        };

        updateConversation(
            conversationId,
            (conversation) => {

                const isFirstUserMessage =
                    !conversation.messages.some(
                        (chatMessage) =>
                            chatMessage.role === "user",
                    );

                return {
                    ...conversation,
                    title: isFirstUserMessage
                        ? createConversationTitle(message)
                        : conversation.title,
                    updatedAt:
                        new Date().toISOString(),
                    messages: [
                        ...conversation.messages,
                        userMessage,
                    ],
                };
            },
        );

        setLoading(true);

        try {

            const result =
                await sendMessage(message);

            const assistantMessage: ChatMessage = {
                id: crypto.randomUUID(),
                role: "assistant",
                recommendation:
                    result.recommendation,
            };

            updateConversation(
                conversationId,
                (conversation) => ({
                    ...conversation,
                    updatedAt:
                        new Date().toISOString(),
                    messages: [
                        ...conversation.messages,
                        assistantMessage,
                    ],
                }),
            );

        } catch (error) {

            console.error(error);

            const errorMessage: ChatMessage = {
                id: crypto.randomUUID(),
                role: "assistant",
                content:
                    "Sorry, something went wrong while contacting the backend.",
            };

            updateConversation(
                conversationId,
                (conversation) => ({
                    ...conversation,
                    updatedAt:
                        new Date().toISOString(),
                    messages: [
                        ...conversation.messages,
                        errorMessage,
                    ],
                }),
            );

        } finally {

            setLoading(false);
        }
    }


    const sortedConversations =
        conversations
            .filter(
                hasUserMessages,
            )
            .sort(
                (first, second) =>
                    new Date(
                        second.updatedAt,
                    ).getTime() -
                    new Date(
                        first.updatedAt,
                    ).getTime(),
            );


    return (

        <div className="app-shell">

            <Navbar />

            <main className="main-content">

                <div className="content-wrapper">

                    <Header
                        title="What would you like to read today?"
                        subtitle="Describe your favorite genres, authors or themes for the perfect book recommendation."
                    />

                    <div className="workspace">

                        <ConversationHistory
                            conversations={sortedConversations}
                            activeConversationId={
                                activeConversation.id
                            }
                            onNewConversation={
                                handleNewConversation
                            }
                            onSelectConversation={
                                handleSelectConversation
                            }
                            onDeleteConversation={
                                handleDeleteConversation
                            }
                        />

                        <div className="chat-section">

                            <div className="chat-card">

                                <ChatWindow
                                    messages={
                                        activeConversation.messages
                                    }
                                    loading={loading}
                                    onSend={handleSend}
                                />

                                <div className="chat-card__footer">

                                    <ChatInput
                                        onSend={handleSend}
                                    />

                                </div>

                            </div>

                        </div>

                    </div>

                </div>

            </main>

        </div>
    );
}


export default App;