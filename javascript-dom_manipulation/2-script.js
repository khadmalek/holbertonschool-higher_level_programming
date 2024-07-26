// Select the red_header element using document.querySelector
const redHeaderElement = document.querySelector('#red_header');

// Select the header element using document.querySelector
const header = document.querySelector('header');

// Define the function to add the red class to the header
function addRedClass() {
  header.classList.add('red');
}

// Add an event listener to red_header that triggers addRedClass on click
redHeaderElement.addEventListener('click', addRedClass);
