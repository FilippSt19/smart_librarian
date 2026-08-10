import axios from "axios";

import type {
    BookArtworkRequest,
    BookArtworkResponse,
    ChatRequest,
    ChatResponse,
} from "../types/chat";


const api = axios.create({
    baseURL:
        import.meta.env.VITE_API_URL ??
        "http://127.0.0.1:8000",
});


export async function sendMessage(
    query: string,
): Promise<ChatResponse> {

    const request: ChatRequest = {
        query,
    };

    const response = await api.post<ChatResponse>(
        "/api/v1/chat",
        request,
    );

    return response.data;
}

export async function generateBookArtwork(
    request: BookArtworkRequest,
): Promise<BookArtworkResponse> {

    const response =
        await api.post<BookArtworkResponse>(
            "/api/v1/images/book-artwork",
            request,
        );

    return response.data;
}