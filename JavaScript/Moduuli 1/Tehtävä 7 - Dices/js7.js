'use strict';

const firstParagraphElement = document.querySelector('p');
const amountOfDices = parseInt(prompt("How many dices would you like to roll?"));
let sum = 0;
let diceRolls = [];

for (let i = 0; i < amountOfDices; i ++) {
    let roll = Math.floor(Math.random() * 6) + 1;
    diceRolls.push(roll);
    sum += roll;
}

firstParagraphElement.textContent = `You decided to roll ${amountOfDices} dices. You got ${diceRolls.join(", ")} and the sum is ${sum}!`;