// Select the red_header element using document.querySelector
const redHeaderElement = document.querySelector('#red_header');

// Select the header element using document.querySelector
const header = document.querySelector('header');

// Define the function to change the header color to red
function changeHeaderColor() {
  header.style.color = '#FF0000';
}

// Add an event listener to red_header that triggers changeHeaderColor on click
redHeaderElement.addEventListener('click', changeHeaderColor);
