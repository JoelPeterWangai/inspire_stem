// Data Types:
/*
1.String,
2.Integers/Numbers
3.Booleans,
4.Arrays
5.
*/
let name = "Joel";
let height = 50

//On click events
// Element selector in JS
function submit(){
var input = document.getElementById("inputfield").value;
var input = input + 1; // Data type conversion
var input = parseInt(input);
console.log(typeof(input))
}

let adult = true; // Boolean data type
let fruits = ['kiwi','pineapple','apple',30,false]
let person ={
    firstname: 'Ada',
    Lastname:  'Lovelace',
    age: 18,
    address:{
        country: 'Sudan',
        city: 'Khartoum',
        street: 'Bani bani',
        
     } ,
    children: ['Kelly','Mary']

}
function saveitem(){
    var input = document.getElementById("inputfield").value
    localStorage.setItem('inputInput',input);
    showWelcomemessage(input)
}
function showWelcomemessage(input){
    var messageLElement=document.getElementById("showmessage")
    messageLElement.textContent = "We have saved your input as"+ input;
}
var storedItem= localStorage.getItem('inputItem');
if(storedItem){
    showWelcomemessage(storedItem)
}
