'use strict';

const year = parseInt(prompt("Give me a year!"));
const firstParagraphElement = document.querySelector('p');

if (year % 4 === 0 && year % 100 !== 0) {
    firstParagraphElement.textContent = `The year ${year} is a leap year!`;
} else if (year % 400 === 0) {
    firstParagraphElement.textContent = `The year ${year} is a leap year!`;
} else {
    firstParagraphElement.textContent = `The year ${year} is not a leap year!`;
}


