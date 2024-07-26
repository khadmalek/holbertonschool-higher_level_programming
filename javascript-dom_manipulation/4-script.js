// Select the element with id 'add_item'
const addItem = document.querySelector('#add_item');

// Select the ul element with class 'my_list'
const list = document.querySelector('.my_list');

// Define the function to add a new li element to the list
function addListItem() {
  // Create a new li element
  const newItem = document.createElement('li');
  // Set the text content of the new li element
  newItem.textContent = 'Item';
  // Append the new li element to the ul
  list.appendChild(newItem);
}

// Add an event listener to the 'add_item' element to call addListItem on click
addItem.addEventListener('click', addListItem);
