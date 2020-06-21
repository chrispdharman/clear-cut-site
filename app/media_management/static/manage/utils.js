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

function init() {
    var media_type_elements = document.getElementsByClassName("media-type-to-name");
    var media_type_index = media_type_elements.length;

    while(media_type_index--) {
        var element = media_type_elements[media_type_index];
        var mediaType = element.getAttribute("data-value");
        element.innerHTML = convertMediaType(mediaType);
    };
}
