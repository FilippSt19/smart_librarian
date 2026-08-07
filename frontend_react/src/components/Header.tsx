import "../styles/header.css";

type HeaderProps = {
    title: string;
    subtitle: string;
};

export default function Header({
    title,
    subtitle,
}: HeaderProps) {

    // Highlight DOAR cuvântul "you"
    const renderTitle = () => {
        if (!title) return title;
        
        const parts = title.split(/(you)/i);
        return parts.map((part, idx) => 
            part.toLowerCase() === "you" 
                ? <span key={idx} className="header__title-highlight">{part}</span>
                : part
        );
    };

    return (
        <header className="header">
            <div className="header__badge">
                AI Book Assistant
            </div>

            <h1 className="header__title">
                {renderTitle()}
            </h1>

            <p className="header__subtitle">
                {subtitle}
            </p>
        </header>
    );
}