// Select the header element using document.querySelector
const header = document.querySelector('header');

// Select the element with id 'update_header'
const updateHeaderButton = document.querySelector('#update_header');

// Define the function to update the header text
function updateHeaderText() {
  header.textContent = 'New Header!!!';
}

// Add an event listener to 'update_header' that triggers updateHeaderText on click
updateHeaderButton.addEventListener('click', updateHeaderText);