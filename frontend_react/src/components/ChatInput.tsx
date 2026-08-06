import { useState } from "react";
import { FaPaperPlane } from "react-icons/fa";

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

                onKeyDown={(e) => {

                    if (e.key === "Enter") {

                        handleSend();

                    }

                }}

                placeholder="Describe the book you are looking for..."

            />

            <button onClick={handleSend}>

                <FaPaperPlane />

            </button>

        </div>

    );

}