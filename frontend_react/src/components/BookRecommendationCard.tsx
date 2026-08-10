import {
    useEffect,
    useState,
} from "react";

import {
    FaStop,
    FaVolumeHigh,
} from "react-icons/fa6";

import type {
    BookRecommendation,
} from "../types/chat";

import "../styles/book-card.css";


type Props = {
    recommendation: BookRecommendation;
};


export default function BookRecommendationCard({
    recommendation,
}: Props) {

    const [isSpeaking, setIsSpeaking] =
        useState(false);


    useEffect(() => {

        return () => {
            window.speechSynthesis?.cancel();
        };

    }, []);


    function handleSpeech() {

        if (!("speechSynthesis" in window)) {
            return;
        }

        if (isSpeaking) {

            window.speechSynthesis.cancel();

            setIsSpeaking(false);

            return;
        }

        window.speechSynthesis.cancel();

        const text = [
            `${recommendation.title}, by ${recommendation.author}.`,
            recommendation.summary,
        ].join(" ");

        const utterance =
            new SpeechSynthesisUtterance(text);

        utterance.lang = "en-US";
        utterance.rate = 1;
        utterance.pitch = 1;

        utterance.onend = () => {
            setIsSpeaking(false);
        };

        utterance.onerror = () => {
            setIsSpeaking(false);
        };

        setIsSpeaking(true);

        window.speechSynthesis.speak(
            utterance,
        );
    }


    return (
        <article className="book-card">

            <div className="book-card__header">

                <div>
                    <span className="book-card__label">
                        Recommended Book
                    </span>

                    <h2 className="book-card__title">
                        {recommendation.title}
                    </h2>

                    <p className="book-card__author">
                        {recommendation.author}
                    </p>
                </div>

                <span className="book-card__genre">
                    {recommendation.genre}
                </span>

            </div>

            <div className="book-card__section">

                <h3>
                    Why this recommendation
                </h3>

                <p>
                    {recommendation.reason}
                </p>

            </div>

            <div className="book-card__section">

                <div className="book-card__section-header">

                    <h3>
                        Complete Summary
                    </h3>

                    <button
                        className={
                            isSpeaking
                                ? "book-card__listen book-card__listen--active"
                                : "book-card__listen"
                        }
                        type="button"
                        onClick={handleSpeech}
                        aria-label={
                            isSpeaking
                                ? "Stop reading summary"
                                : "Read summary aloud"
                        }
                        title={
                            isSpeaking
                                ? "Stop"
                                : "Listen"
                        }
                    >
                        {isSpeaking
                            ? <FaStop />
                            : <FaVolumeHigh />
                        }

                        <span>
                            {isSpeaking
                                ? "Stop"
                                : "Listen"
                            }
                        </span>
                    </button>

                </div>

                <p>
                    {recommendation.summary}
                </p>

            </div>

        </article>
    );
}