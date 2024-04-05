'use strict';

const name = prompt('Syötä nimi:');
console.log(name);

const firstParagraphElement = document.querySelector('p');
firstParagraphElement.textContent = `Moi ${name}`;


