'use strict';

let newNumber = 1;
const numbersList = [];

while (newNumber >= 1) {
    newNumber = parseInt(prompt('Syötä numero (Voit lopettaa syöttämällä 0):'));
    numbersList.push(newNumber);
}
numbersList.sort(function (a, b) {
    return b - a;
})

console.log(numbersList);

