type HeaderProps = {
    title: string;
    subtitle: string;
};

export default function Header({
    title,
    subtitle,
}: HeaderProps) {

    return (
        <header
            style={{
                padding: "24px",
                textAlign: "center",
                background: "#ffffff",
                borderBottom: "1px solid #e5e7eb",
            }}
        >
            <h1
                style={{
                    fontSize: "2rem",
                    marginBottom: "8px",
                }}
            >
                📚 {title}
            </h1>

            <p
                style={{
                    color: "#6b7280",
                }}
            >
                {subtitle}
            </p>
        </header>
    );
}