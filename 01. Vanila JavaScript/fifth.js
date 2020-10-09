/*
if(condition){
    block // this is JS expression. like any conditions..
} else {
    block
}
*/

/*
// it's better not to use prompt function, and I won't use it maybe forever
because I was told that it's really old-fashioned. I can make other fancy things with JS so.. //

const age = prompt("how old are you?");

if (age > 18) {
    console.log("you can drink")
} else {
    console.log("you cannot drink");
}
*/

const title = document.querySelector("#title");
const BASE_COLOR = "white";
const OTHER_COLOR = "#f7b731";

function handleClick() {
    const currentColor = title.style.color;
    console.log(currentColor);
    if (currentColor === BASE_COLOR){
        title.style.color = OTHER_COLOR;
    } else {
        title.style.color = BASE_COLOR;
    }
}

function init(){
    title.style.color = BASE_COLOR;
    title.addEventListener("mouseenter", handleClick);
}

init();

function handleOnline() {
    console.log("how about this?");
};

window.addEventListener("online", handleOnline);
