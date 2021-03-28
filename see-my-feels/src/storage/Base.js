import firebase from 'firebase/app';
import 'firebase/storage';
import App from './../App';

export const app = firebase.initializeApp({
    "projectId": "see-my-feels-db",
    "appId": "1:263420768909:web:0aecfcacb48384da45e8c4",
    "storageBucket": "see-my-feels-db.appspot.com",
    "locationId": "europe-west",
    "apiKey": "AIzaSyCZnI6m9X3vHyI2FhdOqbLRi0-rxAnxuOA",
    "authDomain": "see-my-feels-db.firebaseapp.com",
    "messagingSenderId": "263420768909"
  });

export default App;