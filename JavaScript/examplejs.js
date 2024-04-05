'use strict';

const name = 'Rene';
const names = ['Eemil ', ' Onni', ' Joni'];

let age, height;

age = 5.0;

  //  typeof <value>

console.log(age, height, typeof age, typeof height);
  //  muutetaan number -> string
console.log(age.toString());
  //  age = age.toString(); pysyvästi muuttaa string muotoon
  //  muutetaan string -> number
  //  age = age.parseInt;
  //  age = age.parseFloat;
console.log(age);
  //  age = 'viisi vuotta';
age = parseFloat(age);
console.log(age, typeof age);

const ageAdd = 3;
console.log(age + ageAdd);

console.log(`${name}n ikä on ${age} vuotta`);


const isUnderAge = true;

age = age + 1;
age

console.log(isUnderAge, typeof isUnderAge);

console.log('Moi ' + name);
console.log('Kaikki nimet : '+ names);

const firstParagraphElement= document.querySelector('p');
console.log(firstParagraphElement);
firstParagraphElement.textContent = 'Moi' + name;

const allParagraphElements = document.querySelectorAll('p');
console.log(allParagraphElements);
allParagraphElements[2].textContent = '@';
//alert('JUMPSCARE!');

//let name1 = prompt('Anna nimi');
//firstParagraphElement.textContent = 'Moi ' + name1;

// Math
console.log(Math.random());

//  Arvotaan 1-6 (+1 nostaa 0 yläpuolelle!)
console.log(Math.floor(Math.random()*6+1));
