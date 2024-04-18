'use strict';

const names = ['John', 'Paul', 'Jones'];
const listElement = document.getElementById('target');
let placeholderString = '';

for (let i = 0; i < names.length; i++) {
    placeholderString += '<li>' + names[i] + '</li>';
}

listElement.innerHTML = placeholderString;