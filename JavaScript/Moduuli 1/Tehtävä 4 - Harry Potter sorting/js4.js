'use strict';

let randomHouse = Math.floor(Math.random() * 4) + 1;
const name = prompt("What's your name?")
const firstParagraphElement = document.querySelector('p');

if (name === 'Anna') {
    firstParagraphElement.textContent = `${name}, your Hogwarts house is Ravenclaw!`;
} else if (randomHouse === 1) {
    firstParagraphElement.textContent = `${name}, your Hogwarts house is Gryffindor!`;
} else if (randomHouse === 2) {
    firstParagraphElement.textContent = `${name}, your Hogwarts house is Hufflepuff!`;
} else if (randomHouse === 3) {
    firstParagraphElement.textContent = `${name}, your Hogwarts house is Ravenclaw!`;
} else {
    firstParagraphElement.textContent = `${name}, your Hogwarts house is Slytherin!`;
}