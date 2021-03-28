import logo from './assets/in-my-feels.gif';
import './App.css';
import {FileUploadPage} from './components/Upload'

function App() {
  return (
    <div className="App">
      <div className="Title">
        <h1>See My Feels</h1>
      </div>
      <FileUploadPage />
      <div className="Drake">
        <img src={logo} alt="still loading..."/>
      </div>
    </div>
  );
}

export default App;
