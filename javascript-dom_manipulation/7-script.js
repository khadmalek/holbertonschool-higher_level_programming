// URL to fetch data from
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Select the HTML element where the list of movies will be displayed
const listMoviesElement = document.querySelector('#list_movies');

// Fetch the data from the API
fetch(apiUrl)
  .then((response) => {
    // Check if the response is ok (status code 200-299)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Parse the JSON from the response
    return response.json();
  })
  .then((data) => {
    // Extract the list of films from the data
    const films = data.results;
    // Create a document fragment to hold the list items
    const fragment = document.createDocumentFragment();

    // Iterate over each film and create a list item
    films.forEach((film) => {
      const li = document.createElement('li');
      li.textContent = film.title;
      fragment.appendChild(li);
    });

    // Append the fragment to the ul element
    listMoviesElement.appendChild(fragment);
  })
  .catch((error) => {
    // Handle any errors that occurred during the fetch
    console.error('There has been a problem with your fetch operation:', error);
    listMoviesElement.innerHTML = '<li>Failed to load movie data</li>';
  });