// const title = document.getElementById("title");
// both are the same things
const title = document.querySelector("#title");
// if you put ".title", it means you're finding the class named "title"

// console.log(title);
// console.error('fuck off');
title.innerHTML = "This is from JS";
title.style.color = "yellow";
// console.dir(title);
// console.dir(document);

document.title = "This is my page"

function handleResize(){
    console.log("I've been resized")
}

/*
you SHOULD NOT put () after handleResize
because you're not calling the function right away!
*/ 
window.addEventListener("resize", handleResize)

function handleClick(){
    title.style.color = "white";
}

title.addEventListener("click", handleClick);