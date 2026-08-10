import {
    useEffect,
    useState,
} from "react";

import {
    FaImage,
    FaStop,
    FaVolumeHigh,
} from "react-icons/fa6";

import {
    generateBookArtwork,
} from "../services/api";

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

    const [artwork, setArtwork] =
        useState<string | null>(null);

    const [isGeneratingArtwork, setIsGeneratingArtwork] =
        useState(false);

    const [artworkError, setArtworkError] =
        useState<string | null>(null);


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


    async function handleGenerateArtwork() {

        if (isGeneratingArtwork) {
            return;
        }

        setIsGeneratingArtwork(true);
        setArtworkError(null);

        try {

            const result =
                await generateBookArtwork({
                    title: recommendation.title,
                    author: recommendation.author,
                    genre: recommendation.genre,
                    summary: recommendation.summary,
                });

            setArtwork(
                `data:image/png;base64,${result.image}`,
            );

        } catch (error) {

            console.error(
                "Artwork generation failed.",
                error,
            );

            setArtworkError(
                "Could not generate artwork. Please try again.",
            );

        } finally {

            setIsGeneratingArtwork(false);
        }
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

            <div className="book-card__artwork">

                {artwork && (
                    <img
                        className="book-card__artwork-image"
                        src={artwork}
                        alt={
                            `AI-generated artwork inspired by ${recommendation.title}`
                        }
                    />
                )}

                {artworkError && (
                    <p className="book-card__artwork-error">
                        {artworkError}
                    </p>
                )}

                <button
                    className="book-card__artwork-button"
                    type="button"
                    onClick={handleGenerateArtwork}
                    disabled={isGeneratingArtwork}
                >
                    <FaImage />

                    <span>
                        {isGeneratingArtwork
                            ? "Generating..."
                            : artwork
                                ? "Generate again"
                                : "Generate artwork"
                        }
                    </span>
                </button>

            </div>

        </article>
    );
}