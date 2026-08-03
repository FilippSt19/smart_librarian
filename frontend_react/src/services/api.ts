import axios from "axios";

import type {
    ChatRequest,
    ChatResponse,
} from "../types/chat";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export async function sendMessage(
    request: ChatRequest
): Promise<ChatResponse> {

    const response = await api.post<ChatResponse>(
        "/chat",
        request
    );

    return response.data;
}