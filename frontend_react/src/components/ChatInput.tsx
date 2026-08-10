import {
    useCallback,
    useState,
} from "react";

import {
    FaMicrophone,
    FaPaperPlane,
    FaStop,
} from "react-icons/fa";

import {
    useSpeechRecognition,
} from "../hooks/useSpeechRecognition";


type Props = {
    onSend: (message: string) => void;
};


export default function ChatInput({
    onSend,
}: Props) {

    const [text, setText] =
        useState("");


    const handleTranscript =
        useCallback(
            (transcript: string) => {

                setText((previous) => {

                    if (!previous.trim()) {
                        return transcript;
                    }

                    return `${previous.trim()} ${transcript}`;
                });
            },
            [],
        );


    const {
        isListening,
        isSupported,
        startListening,
        stopListening,
    } = useSpeechRecognition(
        handleTranscript,
    );


    function handleSend() {

        if (!text.trim()) {
            return;
        }

        if (isListening) {
            stopListening();
        }

        onSend(text.trim());

        setText("");
    }


    function handleMicrophone() {

        if (isListening) {
            stopListening();

            return;
        }

        startListening();
    }


    return (

        <div className="chat-input">

            <input
                value={text}

                onChange={(event) =>
                    setText(event.target.value)
                }

                onKeyDown={(event) => {

                    if (event.key === "Enter") {
                        handleSend();
                    }

                }}

                placeholder={
                    isListening
                        ? "Listening..."
                        : "Describe the book you are looking for..."
                }
            />

            {isSupported && (
                <button
                    className={
                        isListening
                            ? "chat-input__microphone chat-input__microphone--active"
                            : "chat-input__microphone"
                    }
                    type="button"
                    onClick={handleMicrophone}
                    aria-label={
                        isListening
                            ? "Stop listening"
                            : "Start voice input"
                    }
                    title={
                        isListening
                            ? "Stop listening"
                            : "Voice input"
                    }
                >
                    {isListening
                        ? <FaStop />
                        : <FaMicrophone />
                    }
                </button>
            )}

            <button
                className="chat-input__send"
                type="button"
                onClick={handleSend}
                aria-label="Send message"
                title="Send"
            >
                <FaPaperPlane />
            </button>

        </div>
    );
}