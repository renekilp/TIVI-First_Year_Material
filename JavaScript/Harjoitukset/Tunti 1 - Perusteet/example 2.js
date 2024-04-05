'use strict';

let userNumber = prompt('Syötä numero:');

if (userNumber % 3 === 0 && userNumber % 5 === 0) {
  console.log(`${userNumber} on jaollinen kolmella ja viidellä.`)
  } else if (userNumber % 3 === 0) {
    console.log(`${userNumber} on jaollinen kolmosella.`)
  } else if (userNumber % 5 === 0) {
  console.log(`${userNumber} on jaollinen vitosella.`)
} else {
    console.log(`${userNumber} ei ole kummallakaan jaettava.`)
  }
