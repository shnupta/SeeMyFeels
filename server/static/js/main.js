// To show overlay when 'generate' button pressed

let processForm = document.getElementById("process-audio");
let overlay = document.getElementById("loading-overlay");
processForm.onsubmit = function() {
  overlay.style.display = "block";
}

// To change context of audio upload button when file has been uploaded

let audioFileInput = document.getElementById("audio-file-input");
let audioInputBtn = document.getElementsByClassName("upload-btn")[0];

function uploadClicked() {
  document.body.onfocus = checkFileSelected;
}

// Function to check if
// the user failed to upload file
function checkFileSelected() {
  setTimeout(function () {
    if (audioFileInput.files.length) {
      audioInputBtn.firstChild.innerHTML = "File Selected";
    }
    document.body.onfocus = null;
  }, 500);
}