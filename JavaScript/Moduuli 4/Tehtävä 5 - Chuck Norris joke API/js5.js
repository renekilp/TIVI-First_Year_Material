'use strict';

fetch('https://api.chucknorris.io/jokes/random')
    .then(response =>{
        return response.json();
    })
    .then(joke =>{
        console.log(joke.value);
    })
