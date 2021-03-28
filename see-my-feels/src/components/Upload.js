import React, { createElement } from 'react';
import ReactDOM from 'react-dom';
import './Upload.css';
import {useForm} from 'react-hook-form';
import {app} from './../storage/Base';
import {FaBeer} from "@react-icons/all-files/fa/FaBeer";
import {FaSmile} from "@react-icons/all-files/fa/FaSmile";

export function FileUpload() {
    const {register, handleSubmit} = useForm();
    var isSubmitted = false;

    const onSubmit = data => {
        console.log(data);
          if (!((data.audio[0].type === 'audio/mpeg') || (data.audio[0].type === 'audio/wav'))) {
            alert("not a valid input!");
            isSubmitted = false;
          } else {
            const storageRef = app.storage().ref();
            const fileRef = storageRef.child(data.audio[0].name);
            fileRef.put(data.audio[0]).then(() => console.log("Uploaded a file"));
            isSubmitted = true;

            var upload_status = document.getElementById("upload-status");
            while (upload_status.hasChildNodes()) {
                upload_status.removeChild(upload_status.firstChild);
            }

            fileRef.getDownloadURL().then((url) => 
                fetch("/process", {
                    method: "POST",
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        'audio-url': url,
                    })
                })
            );
            
            //var node1 = createElement("FaSmile");
            var node2 = document.createTextNode("Uploaded just fine!");
            ReactDOM.render(<FaSmile style={{width:"3em", height:"3em"}} />, document.getElementById("upload-status"));
            document.getElementById("upload-status").appendChild(node2);
          }

    }
    return (
        <div className="FileUpload">
        <div className="Description">
        <p>Ever want to describe the song you love but struggle to find the words?
        Well a picture is the equivalent of 1000 words! Choose the song, 
        and let the magic happen :)</p>
        </div>
        <div className="Form">
        <form onSubmit={handleSubmit(onSubmit)}>
            <input ref={register} required type="file" name="audio" style={{fontSize:"15px"}}/>
            <button style={{transform: "translateX(-20%)", fontSize:"15px"}}>Upload!</button>
        </form>
        </div> 
        { isSubmitted 
        ? <div id="upload-status" style={{paddingTop:"2em", transform:"translateY(10%)"}}><FaSmile id="Child1"/><p id="Child2">Uploaded just fine!</p></div> 
        : <div id="upload-status" style={{paddingTop:"2em", transform:"translateY(10%)"}}><FaBeer style={{width:"3rem", height:"3rem"}} id="Child1" /><p id="Child2">Nothing uploaded yet!</p></div> 
        }
        </div>
    );
  }