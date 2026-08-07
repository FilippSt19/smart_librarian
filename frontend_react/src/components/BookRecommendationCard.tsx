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

                <h3>
                    Complete Summary
                </h3>

                <p>
                    {recommendation.summary}
                </p>

            </div>

        </article>
    );
}