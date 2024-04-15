'use strict';

let numbers = [];

function newNumber() {
  let number;
  while ((number = prompt('Syötä numero:')) !== null) {
    if(numbers.includes(parseInt(number))){
      alert('Et voi syöttää samaa lukua uudestaan! Lopetetaan kysyminen...');
      break;
    } else {
      numbers.push(parseInt(number));
    }
  }
}

newNumber();

const many = numbers.length;
let orderedNumbers = numbers.sort();

console.log(orderedNumbers);