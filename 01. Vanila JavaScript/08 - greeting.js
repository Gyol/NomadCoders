/*
querySelertorAll gets every elements, and puts it into array
let's learn about Local Storage!
*/

const form = document.querySelector(".js-form"),
    input = form.querySelector("input"),
    greeting = document.querySelector(".js-greetings");

const USER_LS = "currentUser";
    SHOWING_CN = "showing";

function paintGreeting(text){
    form.classList.remove(SHOWING_CN)
    greeting.classList.add(SHOWING_CN)
    greeting.innerText = `hello ${text}`
}

function loadName(){
    const currentUser = localStorage.getItem(USER_LS);
    if(currentUser === null){
        // no user here
    } else {
        // a user is here
        paintGreeting(currentUser);
    }
}

function init(){
    loadName();
}

init();