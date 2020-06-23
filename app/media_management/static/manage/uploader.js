function preventDefaults (event) {
    event.preventDefault()
    event.stopPropagation()
}

function handleDragEnter(event) {
    preventDefaults(event);
    document.getElementById('dropzone').style.borderColor = "royalblue";
}

function handleDragLeave(event) {
    preventDefaults(event);
    document.getElementById('dropzone').style.borderColor = "grey";
}

function handleDragOver(event) {
    preventDefaults(event);
    document.getElementById('dropzone').style.borderColor = "royalblue";
}

function handleDrop(event) {
    preventDefaults(event);
    document.getElementById('dropzone').style.borderColor = "grey";

    var files = event.dataTransfer.files;
    handleFiles(files);
}

function handleFiles(files) {
    document.getElementById('file-upload-error').style.display = "none";

    var uploaded_files = document.getElementById('gallery').childNodes;
    
    if (files.length + uploaded_files.length > 1) {
        var error_message = 'Can only upload a single file';
        document.getElementById('file-upload-error').style.display = "block";
        document.getElementById('file-upload-error').innerHTML = error_message;
        throw(error_message);
    }
    Array.from(files).forEach(previewFile);
    // Array.from(files).forEach(includeFileToPayload);
}

function previewFile(file) {
    // Display a preview of the uploaded media
    var reader = new FileReader();

    reader.readAsDataURL(file);
    reader.onloadend = function() {
        var img = document.createElement('img');
        img.src = reader.result;
        document.getElementById('gallery').appendChild(img);
    }
}

window.onload = function() {
    // Dropzone event listeners
    document.getElementById('dropzone').addEventListener('dragenter', handleDragEnter, false);
    document.getElementById('dropzone').addEventListener('dragleave', handleDragLeave, false);
    document.getElementById('dropzone').addEventListener('dragover', handleDragOver, false);
    document.getElementById('dropzone').addEventListener('drop', handleDrop, false);
}
