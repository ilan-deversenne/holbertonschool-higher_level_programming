const header = document.querySelector('header');

document.getElementById('toggle_header').addEventListener('click', () => {
  if (header.classList.contains('green')) {
    header.classList.add('red');
    header.classList.remove('green');
  } else if (header.classList.contains('red')) {
    header.classList.add('green');
    header.classList.remove('red');
  }
});
