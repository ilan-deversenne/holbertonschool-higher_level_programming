const list = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) throw new Error('Failed to get movies');
    return response.json();
  })
  .then(data => {
    data.results.forEach(movie => {
      const el = document.createElement('li');
      el.innerText = movie.title;

      list.appendChild(el);
    });
  })
  .catch(err => {
    console.error(err);
  });
