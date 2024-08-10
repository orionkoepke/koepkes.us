import logo from './logo.svg';
import './Home.css';

export default function Home() {
  return (
    <div className="Home">
      <header className="Home-header">
        <h1>Website Under Construction</h1>
        <img src={logo} className="Home-logo" alt="logo" />
        <p>
          Powered by AWS and React! Test
        </p>
      </header>
    </div>
  );
}
