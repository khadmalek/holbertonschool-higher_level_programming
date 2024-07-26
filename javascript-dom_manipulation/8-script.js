// Define the URL to fetch data from
const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// Define the function to fetch the data and update the HTML element
function fetchAndDisplayHello() {
  // Select the HTML element where the "hello" translation will be displayed
  const helloElement = document.querySelector('#hello');

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
      // Extract the "hello" value from the data
      const helloText = data.hello;
      // Update the text content of the helloElement with the translated "hello"
      helloElement.textContent = helloText;
    })
    .catch((error) => {
      // Handle any errors that occurred during the fetch
      console.error('There has been a problem with your fetch operation:', error);
      helloElement.textContent = 'Failed to load translation';
    });
}

// Execute the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', fetchAndDisplayHello);