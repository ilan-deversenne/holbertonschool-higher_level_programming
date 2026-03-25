document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => {
      if (!response.ok) throw new Error('Failed to get translation');
      return response.json();
    })
    .then(data => {
      document.getElementById('hello').innerText = data.hello;
    })
    .catch(err => {
      console.error(err);
    });
});
