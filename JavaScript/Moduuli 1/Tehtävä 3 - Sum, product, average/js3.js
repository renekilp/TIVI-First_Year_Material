'use strict'

let num1 = parseFloat(prompt('Syötä numero:'));
let num2 = parseFloat(prompt('Syötä toinen numero:'));
let num3 = parseFloat(prompt('Syötä kolmas numero:'));

let sum = num1 + num2 + num3;
let product = num1  * num2 * num3;
let average = sum / 3;

const firstParagraphElement = document.querySelector('p');
firstParagraphElement.textContent = `Syöttämäsi numeroiden: ${num1}, ${num2} ja ${num3} summa: ${sum}, tulo: ${product} ja keskimäärä: ${average}`;