function preventDefaults (event) {
    event.preventDefault()
    event.stopPropagation()
}

function fireRequest(request, callback) {
    // Populate any missing request details with defaults
    url = window.origin.concat(request.endpoint);
    verb = request.verb || 'GET';
    data = request.data || {};

    // Build and send request
    var xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            callback(xhr.response);
        }
    }

    xhr.open(verb, url, false);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', window.csrftoken);
    xhr.send(JSON.stringify(data));
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

function saveItem() {
    // Create item
    var metaElement = document.getElementsByClassName('meta')[0];

    var formData = new Object();
    metaElement.querySelectorAll('.form-control').forEach(function(fieldNode) {
        formData[fieldNode.name] = fieldNode.value;
    });

    console.log('formData', formData);

    item_id = fireRequest({
        endpoint: window.endpoints.processItem,
        verb: 'POST',
        data: formData
    }, saveMedia);
}

function saveMedia(saved_item_response) {
    // Process uploaded media
    var mediaEntries = document.getElementById('gallery').childNodes;
    mediaEntries.forEach(function(mediaEntry) {
        // Hit one of the media uploaded
        fireRequest({
            endpoint: window.endpoints.processMedia,
            verb: 'POST',
            data: {
                image: mediaEntry.src,
                item_id: saved_item_response
            }
        });
    });
}

window.onload = function() {
    // Dropzone event listeners
    document.getElementById('dropzone').addEventListener('dragenter', handleDragEnter, false);
    document.getElementById('dropzone').addEventListener('dragleave', handleDragLeave, false);
    document.getElementById('dropzone').addEventListener('dragover', handleDragOver, false);
    document.getElementById('dropzone').addEventListener('drop', handleDrop, false);
}
