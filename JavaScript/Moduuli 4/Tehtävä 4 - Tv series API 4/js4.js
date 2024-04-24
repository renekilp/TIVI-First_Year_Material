'use strict';

document.getElementById('searchForm').addEventListener('submit', function(event){
  event.preventDefault();

  const inputValue = document.getElementById('query').value;

  fetch(`https://api.tvmaze.com/search/shows?q=${inputValue}`)
    .then(response => {
      if (!response.ok) {
        throw new Error('There was an issue with the network.');
      }
      return response.json();
    })
    .then(data => {
      document.getElementById('results').innerHTML = '';

      data.forEach(result => {
        const article = document.createElement('article');

        const nameHeading = document.createElement('h2');
        nameHeading.textContent = result.show.name;
        article.appendChild(nameHeading);

        const detailsLink = document.createElement('a');
        detailsLink.href = result.show.url;
        detailsLink.textContent = 'Details';
        detailsLink.target = '_blank';
        article.appendChild(detailsLink);

        if (result.show.image) {
          const imageSrc = result.show.image ? result.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
          const image = document.createElement('img');
          image.src = imageSrc;
          image.alt = result.show.name;
          article.appendChild(image);
        }

        const summaryDiv = document.createElement('div');
        summaryDiv.innerHTML = result.show.summary;
        article.appendChild(summaryDiv);

        document.getElementById('results').appendChild(article);
      });
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });
});
