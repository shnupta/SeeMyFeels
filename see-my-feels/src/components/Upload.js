import React from 'react';
import './Upload.css';
import {useForm} from 'react-hook-form';
import {app} from './../storage/Base'

export function FileUpload() {
    const {register, handleSubmit} = useForm();

    const onSubmit = data => {
        console.log(data);
        const storageRef = app.storage().ref();
        const fileRef = storageRef.child(data.audio[0].name);
        fileRef.put(data.audio[0]).then(() => console.log("Uploaded a file"));
    }

    return (
        <div className="FileUpload">
        <form onSubmit={handleSubmit(onSubmit)}>
            <input ref={register} required type="file" name="audio"/>
            <button>Upload!</button>
        </form>
        </div>
    );
  }
//   if (!((this.fileInput.current.files[0].type === 'audio/mpeg') || (this.fileInput.current.files[0].type === 'audio/wav'))) {
//     console.log('you fucked up bro!');
// }

//state = {
    //     selectedFile: null
    // }

    // fileSelectedHandler = event => {
    //     this.setState({
    //         selectedFile: event.target.files[0]
    //     })
    // }

    // fileUploadHandler = event => {
    //     console.log(this.state.selectedFile);
    //     console.log(this.state.selectedFile.name);
    //     if (!((this.state.selectedFile.type === 'audio/mpeg') || (this.state.selectedFile.type === 'audio/wav'))) {
    //         console.log('you fucked up bro!');
    //     }
    // }
  
    // render() {
    //   // highlight-range{5}
    //   return (
    //     <div className="FileUploadPage">
    //     <input type="file" onChange={this.fileSelectedHandler}/>
    //     <button onClick={this.fileUploadHandler}>Upload!</button>
    //     </div>
    //   );
    // }