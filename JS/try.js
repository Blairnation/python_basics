// function detail(){
//    let fullname = prompt('Enter First: ') 
//    console.log(fullname)
// }
// detail()


// function sentence(noun, verb){
//       let word = noun + ' is going ' + verb;
//       return word;

// }

// ans = sentence('Tony', 'school')
// ans2 = sentence('Blair', 'church')
// console.log(ans2)
// console.log(ans)
// console.log()


// let array = [['blair', 27, 'Sunyani'],['nation', 20, 'kumasi']];
// array.push(['ghana', 72, 'West Africa']) // add element to end of the array
// // array.pop()  // remove last element
// // array.shift()  // remove first element
// array.unshift(['kwame', 87, 'accra']) // add element to start of then array

// array[1][1] = 70
// console.log(array[array.length - 1][1])
// console.log(array)

// const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
// let firstName = person.firstName
// let checkName = person['lastName']
// console.log('Name: ', firstName, checkName)
// console.log('Age: ', person.age)


// var globalscope = 509;

// function notglobal(){
//   var checker = 20;
//   console.log(checker)

// }

// function examine(){
//   if (typeof globalscope  != 'undefined'){
//     console.log('I am a global scope ' + 10)
//   }
//   else{
//     console.log('Not a global scope')
//   }
//   if (typeof checker == 'undefined')
//   {
//     console.log("Checker Undefined")
//   }
// }

// examine(); 
// console.log(checker)
// notglobal();


// console.log()
// console.log(typeof('gahna'))
// console.log(typeof(25))
// var man;
// console.log(typeof(man))
// var girl = [];
// console.log(typeof(girl))


// function nextinLine(arr, num){
//      arr.push(num);
//      return arr.shift()

// }

// var arr = [1,2,3,4,5]

// console.log(JSON.stringify(arr))
// console.log( nextinLine(arr, 6))
// console.log(JSON.stringify(arr))

// console.log(20)

// function emps(answer){
//   champ = ''
//   switch(answer){
//     case 'a':
//       champ = 'me'
//       break;
//     case 'b':
//        champ = 'them' 
//        break; 
//     default:
//       champ = 'no one'  
//   }
//   return champ
// }

// // ans = emps(1)
// ans = emps(8)
// console.log(ans)


const person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};

let info = console.log('My full name is ' + person.fullName())

let ant = {firstName:'Adwoa', lastName:'manu'};

console.log(ant.firstName)