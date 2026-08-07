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


export type ChatRequest = {
    query: string;
};


export type ChatResponse = {
    recommendation: BookRecommendation;
};