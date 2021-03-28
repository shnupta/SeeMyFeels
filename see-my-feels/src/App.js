import logo from './assets/in-my-feels.gif';
import './App.css';
import {FileUpload} from './components/Upload'

function App() {
  return (
    <div className="App">
      <div className="Title">
        <h1>See My Feels</h1>
      </div>
      <FileUpload />
      <div className="Drake">
        <img src={logo} alt="still loading..."/>
      </div>
    </div>
  );
}

export default App;
