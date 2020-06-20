function splashImageTransition() {
    document.getElementById("initial-image").style.opacity = 0;
}

function displayLogin() {
    var x = document.getElementsByClassName("login");
    var i;
    for (i = 0; i < x.length; i++) {
        x[i].style.opacity = 1;
    }
}

function init() {
    setTimeout(splashImageTransition, 1000);
    setTimeout(displayLogin, 2600);
}
