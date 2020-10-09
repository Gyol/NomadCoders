function sayHello(yourName, age){
    return `Hello ${yourName} you are ${age} years old`;
}

const greetGyol = sayHello("Gyol", 27)
console.log(greetGyol)


const calculator = {
    plus: function(a, b){
        return a + b;
    },
    minus: function(a, b){
        return a - b;
    },
    multi: function(a, b){
        return a * b;
    },
    div: function(a, b){
        return a / b;
    },
    square: function(a, b){
        return a ** b;
    }
}

const plus5 = calculator.plus(12, 5)
console.log(plus5)
const minus5 = calculator.minus(12, 5)
console.log(minus5)
const multi5 = calculator.multi(12, 5)
console.log(multi5)
const div5 = calculator.div(12, 5)
console.log(div5)
const square5 = calculator.square(12, 5)
console.log(square5)
