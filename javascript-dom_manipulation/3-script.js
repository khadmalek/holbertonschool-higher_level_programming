// Select the header element using document.querySelector
const header = document.querySelector('header');

// Select the toggle_header element using document.querySelector
const toggleHeader = document.querySelector('#toggle_header');

// Define the function to toggle the header class
function toggleHeaderClass() {
  // Check the current class of the header
  if (header.classList.contains('red')) {
    // If the header has class 'red', remove it and add 'green'
    header.classList.remove('red');
    header.classList.add('green');
  } else if (header.classList.contains('green')) {
    // If the header has class 'green', remove it and add 'red'
    header.classList.remove('green');
    header.classList.add('red');
  }
}

// Add an event listener to toggle_header that triggers toggleHeaderClass on click
toggleHeader.addEventListener('click', toggleHeaderClass);
