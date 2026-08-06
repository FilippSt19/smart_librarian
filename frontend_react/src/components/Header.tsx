import "../styles/header.css";

type HeaderProps = {
    title: string;
    subtitle: string;
};

export default function Header({
    title,
    subtitle,
}: HeaderProps) {

    return (

        <header className="header">

            <div className="header__badge">

                AI Book Assistant

            </div>

            <h1 className="header__title">

                {title}

            </h1>

            <p className="header__subtitle">

                {subtitle}

            </p>

        </header>

    );

}