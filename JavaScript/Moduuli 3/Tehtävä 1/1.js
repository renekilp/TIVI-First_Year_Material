'use strict';

const listElement = document.getElementById('target');

const newList = `
<li>First item </li>
<li>Second item</li>
<li>Third Item</li>
`;

listElement.innerHTML = newList;
listElement.classList.add('my-list');