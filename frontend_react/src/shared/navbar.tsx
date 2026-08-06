import { FaBookOpen } from "react-icons/fa";
import { BsStars } from "react-icons/bs";

import "../styles/navbar.css";

export default function Navbar() {

    return (

    <nav className="navbar">

        <div className="navbar__left">

            <div className="navbar__icon">
                <FaBookOpen />
            </div>

            <div>

                <h1 className="navbar__title">
                    Smart Librarian
                </h1>

                <span className="navbar__subtitle">
                    AI Book Recommendation Platform
                </span>

            </div>

        </div>

        <div className="navbar__badge">

            <BsStars />

            <span>Powered by OpenAI</span>

        </div>

    </nav>

);

}