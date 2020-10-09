let a = 240;
const b = a - 5;
a = 4;
console.log(b, a);

const daysOfWeek = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"];
console.log(daysOfWeek[4]);

const gyolInfo = {
    name: "Gyol",
    age: 27,
    gender: "Female",
    isAwesome: true,
    favFood:[
        {
            name: "Udon",
            from: "Japan"
        },
        {
            name: "Kalguksu",
            from: "Korea"
        },
        {
            name: "Maratang",
            from: "China"
        }

    ]
}

console.log(gyolInfo.age)
console.log(gyolInfo.favFood[1])