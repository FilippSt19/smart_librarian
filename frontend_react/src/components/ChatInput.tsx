import { useState } from "react";

type Props = {
    onSend: (message: string) => void;
};

export default function ChatInput({
    onSend,
}: Props) {

    const [text, setText] = useState("");

    function handleSend() {

        if (!text.trim()) {
            return;
        }

        onSend(text);

        setText("");
    }

    return (

        <div className="chat-input">

            <input

                value={text}

                onChange={(e) =>
                    setText(e.target.value)
                }

                placeholder="Ask for a book recommendation..."

            />

            <button onClick={handleSend}>

                Send

            </button>

        </div>

    );
}