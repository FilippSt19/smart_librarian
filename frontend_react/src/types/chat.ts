export type ChatRole =
    | "user"
    | "assistant";


export type BookRecommendation = {
    title: string;
    author: string;
    genre: string;
    reason: string;
    summary: string;
};


export type ChatMessage = {
    id: string;
    role: ChatRole;
    content?: string;
    recommendation?: BookRecommendation;
};


export type Conversation = {
    id: string;
    title: string;
    createdAt: string;
    updatedAt: string;
    messages: ChatMessage[];
};


export type ChatRequest = {
    query: string;
};


export type ChatResponse = {
    recommendation?: BookRecommendation;
    message?: string;
};