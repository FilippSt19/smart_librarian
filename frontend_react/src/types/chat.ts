export type Role = "user" | "assistant";

export interface ChatMessage {
    id: string;
    role: Role;
    content: string;
}

export interface ChatRequest {
    query: string;
}

export interface ChatResponse {
    response: string;
}