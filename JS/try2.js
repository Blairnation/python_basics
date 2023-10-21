// function check(age){
//   if(age <= 15){
//     return "underage"
//   }
//   else if(age > 15 && age <= 40){
//     return "Youth"
//   }
//   else{
//   return 'Old age'
//   }
// }

// console.log(check('41'))

// function check(age){
//   let arr = ['underage', 'youth', 'oldage']
//   switch(age){
//    case 1:
//     return arr[0]
//    case 2:
//     return arr[1]
//     case 3:
//       return arr[2] 
//   }
// }
// console.log(check(3))

// console.log(this)

// let text = "Apple, Banana, Kiwi";
// let part = text.slice(-12, -6);//(7,13)
// let part1 = text.substring(7,13);
// let part2 = text.substr(7, 7);
// console.log(part, part1, part2)

// let text = "Please visit Microsoft and Microsoft!";
// let newText = text.replace("Microsoft", "W3Schools");
// console.log(newText)
// let text2 = text.toUpperCase()
// console.log(text2)
// let stripped = text.charAt(0)
// console.log(stripped)

// let text = "5";
// let padded = text.padStart(4,"x");
// let end_padded = text.padEnd(4,'0')
// console.log(padded, end_padded)


// let text = "Please locate where 'locate' occurs!";
// let index = text.indexOf("locate");
// let index = text.lastIndexOf('locate')
// console.log(index)

// let text = "The rain in SPAIN stays mainly in the plain";
// let ans = text.match("ain");
// console.log(ans)

// let firstName = "John";
// let lastName = "Doe";
// let text = `Welcome ${firstName}, ${lastName}!`;
// console.log(text)

// let x = 9.656;
// console.log(x.toExponential(2));
// console.log(x.toFixed(2));
// console.log(x.valueOf())
// console.log(x.toPrecision(3))

// console.log(Number('john'))
// console.log(Number(false))
// console.log(Number('80'))

// console.log(parseInt("ama 20.44"))

// const cars = [];
// cars[0]= "Saab";
// cars[1]= "Volvo";
// cars[2]= "BMW";
// console.log(cars)

// arr = new Array(10);
// // arr = [10]
// console.log(arr)

// const myGirls = ["Cecilie", "Lone"];
// const myBoys = ["Emil", "Tobias", "Linus"];
// const myChildren = myGirls.concat(myBoys);
// console.log(myChildren)

// const myArr = [[1,2],[3,4],[5,6]];
// const newArr = myArr.flat();
// console.log(newArr)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.splice(2, 0, "Lemon", "Kiwi"); //(index to insert,element to remove(no), elements to insert)
// console.log(fruits)

// const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
// const citrus = fruits.slice(1,3);
// console.log(citrus)

// const arr = [100,20,4,6,1,99,80]
// let sorter = arr.sort(function(a,b){return a -b}) //array sort for numbers
// console.log(sorter)

// const numbers = [45, 4, 9, 16, 25];
// const over18 = numbers.filter(myFunction);
// console.log(over18)
// function myFunction(value) {
//   return value > 18;
// }

// const numbers = [45, 4, 9, 16, 25];
// let sum = numbers.reduce(myFunction);
// console.log(sum)
// function myFunction(total, value) {
//   return total + value;
// }


// const d = new Date("2021-03-25");
// const d = new Date();
// let year = d.getFullYear();
// let year = d.getDate();
// console.log(year)

// console.log(Math.PI)
// console.log(Math.trunc(4.9)

// let rand = Math.floor(Math.random() * 101);//random numbers from 0 to 100
// console.log(rand)

// switch (new Date().getDay()) {
//   case 6:
//     text = "Today is Saturday";
//     break;
//   case 0:
//     text = "Today is Sunday";
//     break;
//   default:
//     text = "Looking forward to the Weekend";
// }
// console.log(text)

// let text = '';
// for (let i=0; i<5; i++){
//   text += 'i am number '+ i + '<br>'
// }
// console.log(text)

// const person = {fname:"John", lname:"Doe", age:25};
// let text = "";
// for (let x in person) {
//   text += person[x];
// }

// const numbers = [45, 4, 9, 16, 25];
// let txt = "";
// for (let x in numbers) {
//   txt += numbers[x];
// }
// console.log(txt)

// const cars = ["BMW", "Volvo", "Mini"];
// let text = "";
// for (let x of cars) {
//   text += x;
// }
// console.log(text)

// let language = "JavaScript";
// let text = "";
// for (let x of language) {
// text += x;
// }
// console.log(text)

// let text= ''
// for (let i = 0; i < 10; i++) {
//   if (i === 3) { break; }
//   text += "The number is " + i + "<br>";
// } console.log(text)


// for (let i = 0, text = ''; i < 10; i++) {
//   if (i === 3) { continue; }
//   text += "The number is " + i + "<br>";
// } console.log(text)

// same code (for, for in, for of, while)
//(
// const cars = ["BMW", "Volvo", "Mini"];

// for (let x of cars){
//   console.log(x)
// }

// let i = 0
// while(i<cars.length){
//   console.log(cars[i])
//   i++;
// }

// for(let x=0; x<cars.length; x++){
//   console.log(cars[x])
// }

// for (let x in cars){
//   console.log(cars[x])
// }
//             )

// const letters = new Set(["a","b","c"]);
// for (const x of letters){
// console.log(x)
// }

// Create a Map
// const fruits = new Map();

// Set Map Values
// fruits.set("apples", 500);
// fruits.set("bananas", 300);
// fruits.set("oranges", 200);
// console.log(fruits)

// const fruits = new Map([
//   ["apples", 500],
//   ["bananas", 300],
//   ["oranges", 200]
// ]);

// for(let x of fruits){
//   console.log(x)
// }
// console.log(fruits)
// console.log(fruits.size)
// console.log(fruits.get('oranges'))
// fruits.delete('bananas')
// console.log(fruits.has('bananas'))


// let voteable = (age < 18) ? "Too young":"Old enough";
// //
// let name = null;
// let text = "missing";
// let result = name ?? text;

// const person = {
//   firstName  : "John",
//   lastName   : "Doe",
//   id         : 5566,
//   myFunction : function() {
//     return this;
//   }
// };
// console.log(person.myFunction())


// const person = {
//   firstName:"John",
//   lastName: "Doe",
//   fullName: function () {
//     return this.firstName + " " + this.lastName;
//   }
// }
// const member = {
//   firstName:"Hege",
//   lastName: "Nilsen",
// }
// let fullName = person.fullName.bind(member);
// console.log(fullName())

// const person1 = {
//   fullName: function() {
//     return this.firstName + " " + this.lastName;
//   }
// }
// const person2 = {
//   firstName:"John",
//   lastName: "Doe",
// }
// let see = person1.fullName.call(person2);
// console.log(see)


// function myFunction() {
//   return this;
// } 
// console.log(myFunction())

// classes
// class Person{
//   constructor(name, age){
//     this.name = name;
//     this.age = age;
//   }
//   get_age(){
//     return this.age
//   }

//   set_height(height){
//     this.height = height
//   }
//   get_height(){
//     return this.height 
//   }
// }

// const person = new Person('Blair', 20)
// console.log(person.name)
// person.set_height(180)
// console.log(person.get_age())
// console.log(person.get_height())


//setters and getters
// setter
// const person = {
//   firstName: "John",
//   lastName: "Doe",
//   language: "",
//   set lang(lang) {
//     this.language = lang
//   }
// };
// person.lang = 'en'
// console.log(person.language)

//getter
// const person = {
//   firstName: "John",
//   lastName: "Doe",
//   language: "en",
//   get lang() {
//     return this.language
//   }
// };
// console.log(person.lang)


// function sumer(){
//   let sum = 0
//   for (i=0;i<arguments.length; i++){
//    sum += arguments[i]
//   }
//   return sum
// }

// let nums = sumer(1,2,3,4,5)
// console.log(nums)