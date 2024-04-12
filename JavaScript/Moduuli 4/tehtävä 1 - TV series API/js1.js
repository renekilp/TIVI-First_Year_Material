'use strict';

document.getElementById('searchForm').addEventListener('submit', function(event){
  event.preventDefault();

  const inputValue = document.getElementById('query').value;

  fetch('INSERT SIVU')
    .then(response => reposponse.json())
    .then(data => {
      console.log(data);
  })
    .catch(error =>)
}