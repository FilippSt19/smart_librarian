import {
    useEffect,
    useRef,
    useState,
} from "react";


type SpeechRecognitionEvent = Event & {
    results: {
        [index: number]: {
            [index: number]: {
                transcript: string;
            };
        };
    };
};


type SpeechRecognitionErrorEvent = Event & {
    error: string;
};


type SpeechRecognitionInstance = EventTarget & {
    lang: string;
    interimResults: boolean;
    continuous: boolean;
    start: () => void;
    stop: () => void;
    abort: () => void;
    onresult:
        | ((event: SpeechRecognitionEvent) => void)
        | null;
    onerror:
        | ((event: SpeechRecognitionErrorEvent) => void)
        | null;
    onend:
        | (() => void)
        | null;
};


type SpeechRecognitionConstructor =
    new () => SpeechRecognitionInstance;


declare global {
    interface Window {
        SpeechRecognition?:
            SpeechRecognitionConstructor;
        webkitSpeechRecognition?:
            SpeechRecognitionConstructor;
    }
}


type UseSpeechRecognitionResult = {
    isListening: boolean;
    isSupported: boolean;
    startListening: () => void;
    stopListening: () => void;
};


export function useSpeechRecognition(
    onTranscript: (transcript: string) => void,
): UseSpeechRecognitionResult {

    const recognitionRef =
        useRef<SpeechRecognitionInstance | null>(
            null,
        );

    const [isListening, setIsListening] =
        useState(false);

    const [isSupported] =
        useState(
            () =>
                "SpeechRecognition" in window ||
                "webkitSpeechRecognition" in window,
        );


    useEffect(() => {

        if (!isSupported) {
            return;
        }

        const Recognition =
            window.SpeechRecognition ??
            window.webkitSpeechRecognition;

        if (!Recognition) {
            return;
        }

        const recognition =
            new Recognition();

        recognition.lang = "en-US";
        recognition.interimResults = false;
        recognition.continuous = false;

        recognition.onresult = (
            event: SpeechRecognitionEvent,
        ) => {

            const transcript =
                event.results[0][0].transcript;

            onTranscript(
                transcript.trim(),
            );
        };

        recognition.onerror = (
            event: SpeechRecognitionErrorEvent,
        ) => {

            console.error(
                "Speech recognition error:",
                event.error,
            );

            setIsListening(false);
        };

        recognition.onend = () => {
            setIsListening(false);
        };

        recognitionRef.current =
            recognition;

        return () => {

            recognition.abort();

            recognitionRef.current = null;
        };

    }, [isSupported, onTranscript]);


    function startListening() {

        if (
            !recognitionRef.current ||
            isListening
        ) {
            return;
        }

        try {

            recognitionRef.current.start();

            setIsListening(true);

        } catch (error) {

            console.error(
                "Could not start speech recognition.",
                error,
            );

            setIsListening(false);
        }
    }


    function stopListening() {

        recognitionRef.current?.stop();

        setIsListening(false);
    }


    return {
        isListening,
        isSupported,
        startListening,
        stopListening,
    };
}