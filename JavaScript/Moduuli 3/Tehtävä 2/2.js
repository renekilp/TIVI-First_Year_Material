'use strict';

const listElement = document.getElementById('target');
const li1 = document.createElement('li');
const li2 = document.createElement('li');
const li3 = document.createElement('li');

li1.textContent = 'First item';
li2.textContent = 'Second item';
li3.textContent = 'Third item';

listElement.appendChild(li1);
listElement.appendChild(li2);
listElement.appendChild(li3);

li2.classList.add('my-item');