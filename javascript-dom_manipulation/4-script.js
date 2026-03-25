const list = document.querySelector('.my_list');

document.getElementById('add_item').addEventListener('click', () => {
  const el = document.createElement('li');
  el.innerText = 'Item';

  list.appendChild(el);
});
