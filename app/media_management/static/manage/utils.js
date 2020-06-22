document.getElementById("display-clear-cuts").onclick = function() {
    // Take all clear cut images to the fore/background
    var clearCutImages = document.getElementsByClassName("clearcut-image");
    var image_index = clearCutImages.length;
    while (image_index--) {
        clearCutImages[image_index].style.zIndex = this.checked ? "1": "0";
    }

    // Set opacity for the toggle icon
    document.getElementById("display-clear-cuts-icon").style.backgroundColor = this.checked ? "white": "coral";
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
                return "image";
            case "2":
                return "video";
            default:
                return "unknown";
        }
    }
}

window.onload = function() {
    parseAllMediaTypes();
}
