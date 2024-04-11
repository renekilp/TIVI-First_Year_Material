'use strict';

const start = prompt("Give me a starting year!");
const end = prompt("Give me an ending year!");
const list = document.querySelector("ul");

for (let i = start; i < end; i ++) {
    const years = document.createElement("li");
    years.innerText = i;
    list.appendChild(years);
}