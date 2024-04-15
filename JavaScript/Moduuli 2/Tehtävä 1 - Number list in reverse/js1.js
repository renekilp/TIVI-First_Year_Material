'use strict';

const numbers = [];
let i = 0;

while (i < 5) {
    numbers.push(prompt('Syötä numero:'));
    i ++;
}

for (let n = numbers.length - 1; n >= 0; n--) {
    console.log(numbers[n]);
}

