'use strict';

const dogNames = [];
let i = 0;

while (i < 6) {
    const dogName = prompt('Syötä koiran nimi:');
    dogNames.push(dogName);
    i ++;
}
dogNames.sort(function (a, b) {
    return b.localeCompare(a);
});

const dogUl = document.createElement('ul');

for (let i = 0; i < dogNames.length; i ++) {
    const name = dogNames[i];
    const dogLi = document.createElement('li');
    dogLi.textContent = name;
    dogUl.appendChild(dogLi);
}

document.body.appendChild(dogUl);

