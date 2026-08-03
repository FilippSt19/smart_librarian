import Navbar from "./shared/navbar";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";

function App() {

    const messages = [
        {
            role: "user" as const,
            content: "I want a fantasy book.",
        },
        {
            role: "assistant" as const,
            content:
                "I recommend The Hobbit because it is a classic fantasy novel.",
        },
    ];

    return (
        <>
            <Navbar />

            <Header
                title="Smart Librarian"
                subtitle="AI Book Recommendation System"
            />

            <ChatWindow
                messages={messages}
            />
        </>
    );
}

export default App;