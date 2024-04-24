'use strict';

document.getElementById('searchForm').addEventListener('submit', function(event){
  event.preventDefault();

  const inputValue = document.getElementById('query').value;

  fetch(`https://api.tvmaze.com/search/shows?q=${inputValue}`)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      data.forEach(result => {
          console.log(result.show.name);
      });
  })
    .catch(error => {
        console.log('There was an issue with the fetch operation.', error);
    });
});