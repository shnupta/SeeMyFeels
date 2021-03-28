import logo from './assets/in-my-feels.gif';
import './App.css';
import {FileUpload} from './components/Upload'
import {Credits} from './components/Credits'
import { FaMusic } from "@react-icons/all-files/fa/FaMusic";

function App() {
  return (
    <div className="App">
      <div className="Title">
        <FaMusic style={{transform:"translateY(70%"}} />
        <h1>See My Feels</h1>
      </div>
      <div className="Drake">
        <img src={logo} alt="still loading..." />
      </div>
      <FileUpload />
      <Credits />
    </div>
  );
}

export default App;
