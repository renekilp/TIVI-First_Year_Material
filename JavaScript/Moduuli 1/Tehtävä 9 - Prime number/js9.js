'use strict';

const number = parseInt(prompt("Give me a number!"));
const firstParagraphElement = document.querySelector('p');
let primeNumber = true;

if (number <= 1) {
    primeNumber = false;
} else {
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            primeNumber = false;
            break;
        }
    }
}

if (primeNumber) {
    firstParagraphElement.textContent = `The number ${number} is a prime number.`;
} else {
    firstParagraphElement.textContent = `The number ${number} is not a prime number.`;
}
