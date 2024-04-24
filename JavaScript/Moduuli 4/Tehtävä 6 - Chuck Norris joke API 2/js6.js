'use strict';

document.getElementById('target').addEventListener('submit', (event) => {
    event.preventDefault();

    const searchValue = document.getElementById('query').value;

    fetch(`https://api.chucknorris.io/jokes/random?category=${searchValue}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('results').innerHTML = '';

            const article = document.createElement('article');
            const jokeText = document.createElement('p');
            jokeText.textContent = data.value;
            article.appendChild(jokeText);
            document.getElementById('results').appendChild(article);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
});
