document.getElementById("display-clear-cuts").onclick = function() {
    if (this.checked) {
        console.log('checkbox was checked?');
    } else {
        console.log('checkbox was unchecked?');
    }
};

function parseAllMediaTypes(params) {
    // Convert all media type values from integers to strings
    var media_type_elements = document.getElementsByClassName("item-media-type");
    var media_type_index = media_type_elements.length;

    while(media_type_index--) {
        var element = media_type_elements[media_type_index];
        var mediaType = element.getAttribute("data-value");
        element.innerHTML = convertMediaType(mediaType);
    };
}

function convertMediaType(params) {
    var media_type_value = params[0];
    if (parseInt(media_type_value) != NaN) {
        switch (media_type_value) {
            case "1":
                return "Image";
            case "2":
                return "Video";
            default:
                return "Unknown";
        }
    }
}

window.onload = function() {
    parseAllMediaTypes();
}
