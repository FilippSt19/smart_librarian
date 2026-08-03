import Navbar from "./shared/navbar";
import Header from "./components/Header";
import ChatMessage from "./components/ChatMessage";

function App() {
    return (
        <>
            <Navbar />

            <Header
                title="Smart Librarian"
                subtitle="AI Book Recommendation System"
            />

            <div
                style={{
                    padding: "32px",
                }}
            >
                <ChatMessage
                    role="user"
                    content="I want a fantasy book."
                />

                <ChatMessage
                    role="assistant"
                    content="I recommend The Hobbit because it is a classic fantasy novel about friendship, courage and adventure."
                />
            </div>
        </>
    );
}

export default App;