'use strict';

const firstParagraphElement = document.querySelector('p');
const calculate = confirm("Should I calculate the square root?");
if (calculate) {
    const number = parseInt(prompt("Give me a number!"));

    if (number < 0) {
        firstParagraphElement.textContent = `the square root of ${number} is not defined!`;
    } else {
        let squareRoot = Math.sqrt(number);
        firstParagraphElement.textContent = `The square root of ${number} is ${squareRoot}!`;

    }
} else {
    firstParagraphElement.textContent = 'The square root is not calculated.';
}