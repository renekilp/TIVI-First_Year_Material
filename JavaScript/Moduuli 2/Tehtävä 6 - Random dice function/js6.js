'use strict';

let diceRolls = []
const print = document.querySelector('ul');
function diceRoll() {
    let num = 0;
    while (num !== 6) {
        num = Math.ceil(Math.random() * 6);
        diceRolls.push(num);
    }
}

diceRoll();

for (let i = 0; i < diceRolls.length; i++) {
  const diceLi = document.createElement('li');
  diceLi.textContent = diceRolls[i];
  print.appendChild(diceLi);
}




