import "../styles/navbar.css";

export default function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar__logo">
                📚 Smart Librarian
            </div>

            <div className="navbar__right">
                AI Book Recommendation System
            </div>
        </nav>
    );
}