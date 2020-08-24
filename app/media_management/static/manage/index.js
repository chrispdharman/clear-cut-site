document.getElementById("display-clear-cuts").onclick = function() {
    var zIndexValue = this.checked ? "1": "0";

    // Take all clear cut images to the fore/background
    var images = document.getElementsByClassName("clearcut-image");
    var image_index = images.length;
    while (image_index--) {
        images[image_index].style.zIndex = zIndexValue;
    }

    // Other toggle display changes
    if (this.checked) {
        document.getElementById("display-clear-cuts-icon").style.backgroundColor = "white";
        document.getElementById("display-clear-cuts-text").innerHTML = "Toggle: Original";
    } else {
        document.getElementById("display-clear-cuts-icon").style.backgroundColor = "paleturquoise";
        document.getElementById("display-clear-cuts-text").innerHTML = "Toggle: ClearCut";
    }
};

document.getElementById("display-spread").onclick = function() {
    // Translate all original images (and turn off hover behaviour)
    var images = document.getElementsByClassName("original-image");
    var image_index = images.length;
    while (image_index--) {
        if (this.checked) {
            images[image_index].style.transform = "translate(0, -".concat(images[image_index].height/2).concat("px)");
        } else {
            images[image_index].style.transform = "translate(0, 0)";
        }
    }

    // Translate all clear cut images (and turn off hover behaviour)
    var images = document.getElementsByClassName("clearcut-image");
    var image_index = images.length;
    while (image_index--) {
        if (this.checked) {
            images[image_index].style.transform = "translate(0, ".concat(images[image_index].height/2).concat("px)");
        } else {
            images[image_index].style.transform = "translate(0, 0)";
        }
    }

    // Other toggle display changes
    if (this.checked) {
        document.getElementById("display-spread-icon").style.backgroundColor = "white";
        document.getElementById("display-spread-text").innerHTML = "View: Single";
    } else {
        document.getElementById("display-spread-icon").style.backgroundColor = "paleturquoise";
        document.getElementById("display-spread-text").innerHTML = "View: Spread";
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
