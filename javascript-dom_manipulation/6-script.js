// URL to fetch data from
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Select the HTML element where the character name will be displayed
const characterElement = document.querySelector('#character');

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
    // Extract the character name from the data
    const characterName = data.name;
    // Update the text content of the characterElement with the character name
    characterElement.textContent = characterName;
  })
  .catch((error) => {
    // Handle any errors that occurred during the fetch
    console.error('There has been a problem with your fetch operation:', error);
    characterElement.textContent = 'Failed to load character data';
  });