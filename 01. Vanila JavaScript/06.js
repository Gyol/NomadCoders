const title = document.querySelector("#title");

const CLICKED_CLASS = "clicked";

/* 
// I could write it in this way.. but not recommended //
function handleClick() {
    const currentClass = title.className;
    if(currentClass !== CLICKED_CLASS){
        title.className = CLICKED_CLASS;
    } else {
        title.className = "";
    }
}
so I had to change this like the one below //
*/ 

/*
// This is okay.. but! There is still another method for this //
function handleClick() {
    const hasClass = title.classList.contains(CLICKED_CLASS);
    if (!hasClass) {
        title.classList.add(CLICKED_CLASS);
    } else {
        title.classList.remove(CLICKED_CLASS);
    }
}
// and that is called 'toggle' //
*/

function handleClick() {
    title.classList.toggle(CLICKED_CLASS)
}

function init() {
    title.addEventListener("click", handleClick);
}

init();