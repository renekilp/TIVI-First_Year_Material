'use strict';

const trigger = document.getElementById('trigger');
const targetImg = document.getElementById('target');
const originalImg = targetImg.src;
const newImg = 'img/picB.jpg';

trigger.addEventListener('mouseover', ()=>{
    targetImg.src = newImg;
});

trigger.addEventListener('mouseout', () => {
    targetImg.src = originalImg;
});