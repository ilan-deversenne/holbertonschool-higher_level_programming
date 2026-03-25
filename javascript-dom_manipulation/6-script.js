const character = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to get data');
        }
        return response.json();
    })
    .then(data => {
        character.innerText = data['name'];
    })
    .catch(err => {
        console.error(err);
    });
